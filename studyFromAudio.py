import pvporcupine
import webbrowser
import time

import pyaudio
import struct

chatgpt = 'https://chatgpt.com/'
calculus = 'https://tutorial.math.lamar.edu/classes/calciii/calciii.aspx'
circuitry = 'https://neuron.eng.wayne.edu/ECE330/Practical_Electronics_for_Inventors.pdf'
physics = 'https://salmanisaleh.wordpress.com/wp-content/uploads/2019/02/physics-for-scientists-7th-ed.pdf'

porcupine = pvporcupine.create(
    access_key = "nQznlljF2uUHKiHaVrKT2kdWNaTuSJEq6gMCKcMsIaBzhHLQ6B6t9A==",
    keyword_paths = ['C:\\Users\\USER\\Desktop\\KeyWords\\study_en_windows_v3_0_0\\study.ppn']
)

pa = pyaudio.PyAudio()

audio_stream = pa.open(
    rate = porcupine.sample_rate,
    channels = 1,
    format = pyaudio.paInt16,
    input = True,
    frames_per_buffer = porcupine.frame_length
)

print("Listening...")

try:
    
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if(keyword_index >= 0):
            webbrowser.open(chatgpt)
            time.sleep(1.7)
            webbrowser.open(physics)
            time.sleep(1.7)
            webbrowser.open_new(circuitry)
            time.sleep(1.7)
            webbrowser.open_new_tab(calculus)
            time.sleep(2)
            quit()
finally:
    audio_stream.close()
    pa.terminate()
    porcupine.delete()

