import sounddevice as sd
import numpy    

#initial conditions
duration = 4
sample_rate = 44000

#Record
print("Start")
audio = sd.rec(int(duration * sample_rate), samplerate= 44000, channels= 1, dtype= 'float32')
sd.wait()
print("done")

#Write recorded audio as an audio file
import scipy.io.wavfile as wav
wav.write("test.wav", 44000, audio)


#Play the recorded audio
print("playing audio")
sd.play(audio, 44000)
sd.wait()
print("done")


