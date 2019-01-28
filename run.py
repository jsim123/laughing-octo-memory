from app import app
from flask_socketio import SocketIO
socketio = SocketIO(app)

import routes

if __name__ == '__main__':

	socketio.run(app,port=3000)
