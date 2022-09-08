import pyaudio
import wave
import time


def recorde(rt):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=4096, input_device_index=1)
    frames = []
    timeout = time.time() + rt
    while True:
        data = stream.read(4096)
        frames.append(data)
        if data == rt or time.time() > timeout:
            break

    stream.stop_stream()
    stream.close()
    audio.terminate()

    sound_file = wave.open("hmm.wav", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
