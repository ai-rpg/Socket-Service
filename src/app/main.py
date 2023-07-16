from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from config import HTTPPORT, BUILD_VERSION, METRICS_PATH, NAME, HOST
from metrics import WEBSOCKET_ACTIVE, BASE_ROOT_CALLED, WEBSOCKET_MSGS_RECEIVED
from logger import log
from datetime import datetime
from services.ai_service import AIService
from domain.game_caches_model import GameCache, GameCacheList

app = Flask(__name__)

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


class WebSocketServer:
    def __init__(self, ai_service=None):
        if ai_service is None:
            self.ai_service = AIService()
        else:
            self.ai_service = ai_service

        self.games = GameCacheList()

    def base_root(self):
        log.debug("base route called", extra={"tags": {"application": NAME}})
        BASE_ROOT_CALLED.inc()
        data = {"data": "This text was fetched using an HTTP call to server on render"}
        return jsonify(data)

    def connected(self):
        WEBSOCKET_ACTIVE.inc()
        self.games.games.append(GameCache('1', request.sid, ''))
        pass

    def message(self, data):
        currentgame = [game for game in self.games.games if game.get('sid')==request.sid][0]

        WEBSOCKET_MSGS_RECEIVED.inc()
        pass

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

@app.route("/msg", methods=['POST'])
def handle_api_message():
    request.sid = "1"
    return web_socket_server.message(request.get_json())


if __name__ == "__main__":
    socketio.run(app, port=int(HTTPPORT), host=HOST)