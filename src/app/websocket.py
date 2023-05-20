from flask import Flask, request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS
from config import BUILD_VERSION, METRICS_PATH, NAME, OPENAPIKEY
from logger import log

from adapter.game_details_repository import GameDetailsRepository
from adapter.prompt_repository import PromptRepository
from services.ai_service import AIService
from services.ai_summary_service import AISummaryService
from services.fate_service import FateService
from services.nlp_service import NlpService
from datetime import datetime
app = Flask(__name__)

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

#nlp = NlpService()
fate_service = FateService()
game_defails_respository = GameDetailsRepository()
prompt_repository = PromptRepository()
dm_ai = AIService()
summary_ai = AISummaryService()
nicknames = {}

# work out a better way
history = []
summary = {}


@app.route("/http-call")
def http_call():
    """return JSON with string data as the value"""
    data = {'data':'This text was fetched using an HTTP call to server on render'}
    return jsonify(data)

@socketio.on("connect")
def connected():
    emit("connect",{"data":f"id: {request.sid} is connected"})
    emit("message",{'text':"Creating game",'from':'DM', 'created': str(datetime.now())},broadcast=True)
    """event listener when client connects to the server"""
    print(request.sid)
    print("client has connected")
    # game_details = game_defails_respository.get()
    # base_prompt = prompt_repository.generate(game_details)
    # dm_response = dm_ai.get_response(base_prompt.prompt_string)
    # history.append(dm_response)

    # emit("message",{'text':dm_response,'from':'DM', 'created': str(datetime.now())},broadcast=True)
    # summary['main'] = summary_ai.get_summary(' '.join(history))

@socketio.on('set-nickname')
def setNickname(data):
    nicknames[request.sid] = data
    if len(nicknames) == 1:
        game_details = game_defails_respository.get()
        base_prompt = prompt_repository.generate(game_details)
        dm_response = dm_ai.get_response(base_prompt.prompt_string)
        history.append(dm_response)
        emit("message",{'text':dm_response,'from':'DM', 'created': str(datetime.now())},broadcast=True)
        summary['main'] = summary_ai.get_summary(' '.join(history))

    emit("users-changed", {'user':data, 'event': 'joined'})

@socketio.on('add-message')
def handle_message(data):
    """event listener when client types a message"""
    print("data from the front end: ",str(data))
    emit("message",{'text':str(data['text']),'from':nicknames[request.sid], 'created': str(datetime.now())},broadcast=True)
    dm_response = dm_ai.get_response(summary['main'] + "  " + data['text'])
    history.append(dm_response)
    emit("message",{'text':dm_response,'from':'DM', 'created': str(datetime.now())},broadcast=True)
    summary['main'] = summary_ai.get_summary(' '.join(history))

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)

if __name__ == '__main__':
    socketio.run(app,port=5001, host="0.0.0.0")