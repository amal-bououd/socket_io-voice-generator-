import socketio
import time
import subprocess

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.on('event_1')
def my_message(data-event_1):
    print('message received with ', data-event_1)

    trigger_vocal_alert(data-event_1, language="en", voice_variant="f4", speed=150, pitch=70, volume=80)

@sio.on('event_2')
def my_messages(data-event_2):
    print('message received with ', data-event_2)

    trigger_vocal_alert(data-event_2, language="en", voice_variant="f4", speed=150, pitch=70, volume=80)


def trigger_vocal_alert(text, language="en", voice_variant=None, speed=120, pitch=50, volume=100):
    voice_option = language
    if voice_variant:
        voice_option += "+" + voice_variant  # Use "+" instead of "-"
    command = ["espeak", "-s", str(speed), "-v", voice_option, "-p", str(pitch), "-a", str(volume), text]
    subprocess.run(command)
 
@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://server_IP:port')
sio.wait()
