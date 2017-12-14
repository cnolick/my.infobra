#!/usr/bin/env python
import config
from threading import Lock
from utils.support import random_list_contact
from utils.health import check_os
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
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

@app.route('/')
def index():
    return render_template('index.html',
                           async_mode=socketio.async_mode,
                           name=config.name,
                           title=config.title,
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



if __name__ == '__main__':
    socketio.run(app, debug=True)