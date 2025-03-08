import sounddevice as sd
import numpy    

'''Starting parameters'''
audio_time = 4
sample_rate = 44000

'''Start recording'''
print("Start")
audio = sd.rec(int(audio_time * sample_rate), samplerate= 44000, channels= 1, dtype= 'float32')
sd.wait()
print("done")

'''Start writing the audio file'''
import scipy.io.wavfile as wav
wav.write("test.wav", 44000, audio)


'''Finally, play the created audio file'''
print("playing audio")
sd.play(audio, 44000)
sd.wait()
print("end")


