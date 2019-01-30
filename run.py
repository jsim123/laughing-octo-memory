from app import app
from flask_socketio import SocketIO,send, emit

socketio = SocketIO(app)

import routes

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('play')
def handle_played(json):
    print('Video has' + str(json))
    socketio.emit('playVid',broadcast=True)



@socketio.on('pause')
def handle_paused(json):
    print('Video has' + str(json))
    socketio.emit('pauseVid',broadcast=True)

@socketio.on('buffering')
def handle_buffer(json):
    print('Video has buffered at' + str(json))
    socketio.emit('buffervid',json,broadcast=True)


if __name__ == '__main__':

    socketio.run(app,port=3000)
