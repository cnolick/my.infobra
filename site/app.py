#!/usr/bin/env python
import config
import os
import binascii
from threading import Lock
from multiprocessing import Value
import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

counter = Value('i', 0)

async_mode = None

app = Flask(__name__)
key = binascii.hexlify(os.urandom(24))
app.config['SECRET_KEY'] = str(key)
print(key)
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

def contact():
    while True:
        if config.social_block == True:
            linkedin = f"""<a href="{config.facebook}" class="fa fa-linkedin"></a>"""
            github = f"""<a href="{config.github}" class="fa fa-github"></a>"""
            twitter = f"""<a href="{config.twitter}" class="fa fa-twitter"></a>"""
            facebook = f"""<a href="{config.facebook}" class="fa fa-facebook"></a>"""
            mail = f"""<a href="mailto:{config.email}" class="fa fa-envelope"></a>"""
            foo = [linkedin, github, twitter, facebook, mail]
            random.shuffle(foo)
        else:
            foo = [f"""<a href="mailto:{config.email}" class="fa fa-envelope"></a>"""]
        #oo = 'hello'
        socketio.sleep(3)
        socketio.emit('resp',
                        {'social': foo},
                        namespace='/get')

@app.route('/')
def index():
    with counter.get_lock():
        counter.value += 1
    return render_template('index.html',
                        async_mode=socketio.async_mode,
                        name=config.name,
                        title=config.domain+" || "+config.name,
                           count_u=counter.value)


@app.route('/info')
def info():
    return render_template('me.html',
                           async_mode=socketio.async_mode,
                           name=config.name,
                           title=config.domain+" || "+config.name)


@socketio.on('connect', namespace='/get')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=contact)



if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
