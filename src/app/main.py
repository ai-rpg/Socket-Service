from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from config import HTTPPORT, BUILD_VERSION, METRICS_PATH, NAME, HOST
from metrics import WEBSOCKET_ACTIVE, BASE_ROOT_CALLED, WEBSOCKET_MSGS_RECEIVED
from logger import log
from datetime import datetime
from services.ai_service import AIService
from adapter.redis_repository import RedisRepository
from domain.game_caches_model import GameCache
import json

app = Flask(__name__)

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


class WebSocketServer:
    def __init__(self, ai_service=None, redis_repository=None):
        if ai_service is None:
            self.ai_service = AIService()
        else:
            self.ai_service = ai_service

        if redis_repository is None:
            self.redis_repository = RedisRepository()
        else:
            self.redis_repository = redis_repository

    def base_root(self):
        log.debug("base route called", extra={"tags": {"application": NAME}})
        BASE_ROOT_CALLED.inc()
        data = {"data": "This text was fetched using an HTTP call to server on render"}
        return jsonify(data)

    def connected(self):
        WEBSOCKET_ACTIVE.inc()
        self.redis_repository.set(GameCache("1", request.sid, []))


    def message(self, data):
        log.info("message", extra={"tags": {"application": NAME}})
        cache = self.redis_repository.get('1')
        WEBSOCKET_MSGS_RECEIVED.inc()
        holder = json.loads(cache)
        current_game = GameCache(holder['user_id'], holder['sid'], holder['gamelog'])
        current_game.gamelog.append(data)
        self.redis_repository.set(current_game)
        responce = self.ai_service.request_from_ai(current_game.gamelog)
        current_game.gamelog.append("{'role':'system', 'content':"+responce.text+"}")
        log.info(current_game.toJSON(), extra={"tags": {"application": NAME}})
        return current_game.toJSON()

    def disconnect(self):
        WEBSOCKET_ACTIVE.dec()
        pass


web_socket_server = WebSocketServer()


@socketio.on("connect")
def connected():
    web_socket_server.connected()


@socketio.on("message")
def handle_message(data):
    return web_socket_server.message(data=data)


@app.route("/")
def base_root():
    request.sid = "1"
    web_socket_server.connected()
    return web_socket_server.base_root()


@app.route("/msg", methods=["POST"])
def handle_api_message():
    request.sid = "1"
    return web_socket_server.message(request.get_json())


if __name__ == "__main__":
    log.info("Application Starting up", extra={"tags": {"application": NAME}})
    socketio.run(app, port=int(HTTPPORT), host=HOST)
