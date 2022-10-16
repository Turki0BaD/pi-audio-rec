import pyaudio
import wave
import time
from datetime import datetime


def recorde(rt):
    # Adding the setting and inputting the devices for the recording
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=4096,
                        input_device_index=1)
    frames = []
    # The timer for the recording and the recording
    timeout = time.time() + rt
    while True:
        data = stream.read(4096)
        frames.append(data)
        if data == rt or time.time() > timeout:
            break
    # Adding a live time feed
    S = datetime.now()
    CT = S.strftime('%m-%d %H;%M')
    # Stopping the recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Saving the output into a wave file
    sound_file = wave.open(CT + ".wav", "wb")  # This line is used to name the files
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
