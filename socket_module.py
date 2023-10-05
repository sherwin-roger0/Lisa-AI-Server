# socket_module.py
from flask import Flask,session
from flask_socketio import SocketIO,join_room

# Create a Socket.IO instance
socketio = SocketIO(cors_allowed_origins="*")


@socketio.on('connect')
def handle_connect():
    print("Connected")
    
@socketio.on('join_room')
def handle_connect(data):
    session["room"]=data
    join_room(session["room"]) 
    print(session["room"])

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')