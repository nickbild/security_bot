import cv2


camera = cv2.VideoCapture(0)

_, image = camera.read()
cv2.imwrite('img.jpg', image)








import pyaudio
import wave

form_1 = pyaudio.paInt16
chans = 1
samp_rate = 16000
chunk = 512
record_secs = 2
dev_index = 1
wav_output_filename = 'test1.wav'

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
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
