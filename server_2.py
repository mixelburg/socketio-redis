## app.py

from eventlet import monkey_patch

monkey_patch()
from flask_socketio import SocketIO
from flask import Flask
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

REDIS_URL = f"redis://127.0.0.1:6379/0"
print(f'REDIS_URL: {REDIS_URL}')
app.logger.info(f"Connecting SocketIO to redis at {REDIS_URL}")
sio = SocketIO(app, message_queue=REDIS_URL, logger=True, engineio_logger=True)

PORT = 5001


@app.route("/")
def root():
    return "hello world"


if __name__ == "__main__":
    try:
        sio.run(app, host="0.0.0.0", port=PORT)
        # pause on control-c
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting...")
