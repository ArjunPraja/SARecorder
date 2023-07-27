import pyaudio
import wave
import time

def record_audio(duration):
    filename= "recorded_audio.wav"
    chunk = 1024
    channels = 2
    sample_format = pyaudio.paInt16
    frames_per_second = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=sample_format,
                        channels=channels,
                        rate=frames_per_second,
                        frames_per_buffer=chunk,
                        input=True)

    print("Recording audio...")

    frames = []
    for i in range(int(frames_per_second / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(sample_format))
    wf.setframerate(frames_per_second)
    wf.writeframes(b"".join(frames))
    wf.close()

