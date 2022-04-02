import socketio

# standard Python
sio = socketio.Client()

print("Connecting to server...")
sio.connect('http://localhost:5001')


@sio.on('response')
def on_response(data):
    print("Received response:", data)

