import pvporcupine
import pyaudio
import struct

'''Access Porcupine Api'''
porcupine = pvporcupine.create(
  access_key='secret-api-key',
  keyword_paths=['Path-to-keyword-file']
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
        '''Take a single frame from the microphone'''
        pcm = audio_stream.read(porcupine.frame_length)
        '''Unpack said frame'''
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        '''Let porcupine process the frame'''
        keyword_index = porcupine.process(pcm)

      '''If porcupine detects the frame to be the keyword, then let the user know'''
        if keyword_index >= 0:
            print("recognized keywords")
            '''Once the Key Word is detected, then close the input stream'''
            break

finally:
    '''Once the Key Word is detected, then close the input stream'''
    audio_stream.close()
    pa.terminate()
    porcupine.delete()
