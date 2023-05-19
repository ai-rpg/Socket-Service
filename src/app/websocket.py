from flask import Flask, request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/http-call")
def http_call():
    """return JSON with string data as the value"""
    data = {'data':'This text was fetched using an HTTP call to server on render'}
    return jsonify(data)

@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print(request.sid)
    print("client has connected")
    emit("connect",{"data":f"id: {request.sid} is connected"})

@socketio.on('add-message')
def handle_message(data):
    """event listener when client types a message"""
    print("data from the front end: ",str(data))
    emit("message",{'text':data['text'],'id':request.sid},broadcast=True)

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)

if __name__ == '__main__':
    socketio.run(app,port=5001, host="0.0.0.0")