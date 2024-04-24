
# Socket.IO Voice Generator

This Python script utilizes the Socket.IO library to receive events from a server and trigger vocal alerts using the `espeak` command-line tool in Ubuntu.

## Prerequisites

- Python 3.x
- `socketio` Python library
- `espeak` command-line tool (install using `sudo apt install espeak`)

## Installation

1. Clone this repository:

git clone git@github.com:amal-bououd/socket_io-voice-generator-.git

## Usage

Run the script:
python3 voice_generator.py
The script will establish a connection with the Socket.IO server specified in the code (http://server_IP:port). It listens for two events:
event_1: Triggers a vocal alert when received.
event_2: Triggers a vocal alert when received.
Customize the voice options (language, voice variant, speed, pitch, volume) in the trigger_vocal_alert function according to your preferences.
The script will print messages to the console when events are received and when the connection is established or disconnected.

## Configuration

You can modify the server URL (http://server_IP:port) in the sio.connect() function call to connect to a different Socket.IO server.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests
