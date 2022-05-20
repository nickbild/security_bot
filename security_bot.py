import pyaudio
import wave
import time
from scipy.io.wavfile import read
import numpy
import glob
import subprocess


def check_for_audio_anomaly():
    form_1 = pyaudio.paInt16
    chans = 1
    samp_rate = 16000
    chunk = 512
    record_secs = 1
    dev_index = 1

    audio = pyaudio.PyAudio()

    # Record audio from microphone.
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)

    frames = []
    # Loop through stream and append audio chunks to frame array.
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop the stream, close it, and terminate the pyaudio instance.
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the audio frames as .wav file.
    wavefile = wave.open("audio_sample.wav", 'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    # Prepare the audio data for ML model input.
    wav_handle = read("audio_sample.wav")
    wav_data = numpy.array(wav_handle[1],dtype=float)

    out = open("audio_sample.txt", "w")

    for i in range (len(wav_data)):
        out.write("{0}\n".format(wav_data[i]))

    # Zero padding.
    for i in range (794):
        out.write("0\n")

    out.close()

    # Call Edge Impulse anomaly detection model.
    return subprocess.check_output(['./audio_anomaly_detection/build/app']).decode('UTF-8')
    

def main():
    while(True):
        anomaly_score = check_for_audio_anomaly()
        print(anomaly_score)


if __name__ == "__main__":
    main()
