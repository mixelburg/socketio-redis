## app.py
from eventlet import monkey_patch

monkey_patch()
from flask_socketio import SocketIO, emit
from flask import Flask, render_template
import logging


app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

REDIS_URL = f"redis://localhost:6379/0"
app.logger.info(f"Connecting SocketIO to redis at {REDIS_URL}")
sio = SocketIO(app, message_queue=REDIS_URL, logger=True, engineio_logger=True)


@sio.on("echo")
def handle_message(message):
    app.logger.info(f"received message: {message}")
    emit("response", {"text": "hello world", "request": message["data"]})


@app.route("/")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    sio.run(app, host="0.0.0.0")