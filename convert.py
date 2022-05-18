from scipy.io.wavfile import read
import numpy
import glob


for f in glob.glob("audio_data/normal_*.wav"):
    a = read(f)
    b = numpy.array(a[1],dtype=float)

    new_file = f.split("/")
    new_file = new_file[-1].replace(".wav", ".csv")
    out = open("audio_data/processed/{0}".format(new_file), "w")
    out.write("timestamp,intensity\n")

    ts = 0
    for i in range (len(b)):
        out.write("{0},{1}\n".format(round(ts, 2), b[i]))
        ts += 0.063

    out.close()

