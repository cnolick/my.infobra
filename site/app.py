#!/usr/bin/env python
import config
from threading import Lock
from utils.support import random_list_contact
from utils.health import check_os, disk_space
from flask import Flask, render_template
from flask_socketio import SocketIO, emit



async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

def contact():
    while True:
        socketio.sleep(3)
        socketio.emit('resp',
                      {'contacts': random_list_contact()},
                      namespace='/test')

def health_size():
    while True:
        socketio.sleep(1)
        socketio.emit('resp_health',
                      {'health_size': disk_space()},
                      namespace='/health')



@app.route('/')
def index():
    return render_template('index.html',
                           async_mode=socketio.async_mode,
                           name=config.name,
                           title=config.domain+"||"+config.name,
                           os=check_os())


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=contact)



@socketio.on('my_ping', namespace='/ping')
def ping_pong():
    emit('my_pong')


@socketio.on('health', namespace='/health')
def health_monitor():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=health_size)



if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)