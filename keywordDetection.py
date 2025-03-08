import pvporcupine
import pyaudio
import struct

'''Access Porcupine Api'''
porcupine = pvporcupine.create(
  access_key='nQznlljF2uUHKiHaVrKT2kdWNaTuSJEq6gMCKcMsIaBzhHLQ6B6t9A==',
  keyword_paths=['C:\\Users\\USER\\Desktop\\KeyWords\\Friday_en_windows_v3_0_0\\Friday.ppn']
)

pa = pyaudio.PyAudio()
'''Stream settings'''
audio_stream = pa.open(
    rate = porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

print("Listening for wake word...")
'''Listening for Wake Word'''
try:
    '''As long as the Input is hearing, check for the Key Word and label the index as such'''
    while True:
        # Read a frame from the microphone
        pcm = audio_stream.read(porcupine.frame_length)
        '''Unpack said frame'''
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        # Process the frame with Porcupine
        keyword_index = porcupine.process(pcm)

        # Check if the frame contains the Key Word
        if keyword_index >= 0:
            print("recognized keywords")
            '''Once the Key Word is detected, then close the input stream'''
            break

finally:
    '''Once the Key Word is detected, then close the input stream'''
    # Clean up
    audio_stream.close()
    pa.terminate()
    porcupine.delete()
