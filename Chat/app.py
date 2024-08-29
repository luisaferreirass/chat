from flask import Flask, render_template
from flask_socketio import SocketIO




app = Flask(__name__)
socketio= SocketIO(app)

@app.route('/')
def page():
    return render_template('index.html')

@socketio.on('message')
def handle_connection(msg):
    print(msg)




if __name__ == '__main__':
    socketio.run(app, debug=True)
