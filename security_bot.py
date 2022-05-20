import pyaudio
import wave
import time
from scipy.io.wavfile import read
import numpy
import glob
import os


form_1 = pyaudio.paInt16
chans = 1
samp_rate = 16000
chunk = 512
record_secs = 1
dev_index = 1


def check_for_audio_anomaly():
    audio = pyaudio.PyAudio()

    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)

    frames = []
    # Loop through stream and append audio chunks to frame array.
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop the stream, close it, and terminate the pyaudio instantiation.
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open("audio_sample.wav", 'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    a = read("audio_sample.wav")
    b = numpy.array(a[1],dtype=float)

    out = open("audio_sample.txt", "w")

    for i in range (len(b)):
        out.write("{0}\n".format(b[i]))

    # Zero padding.
    for i in range (794):
        out.write("0\n")

    out.close()

    os.system("./audio_anomaly_detection/build/app")


while(True):
    check_for_audio_anomaly()
