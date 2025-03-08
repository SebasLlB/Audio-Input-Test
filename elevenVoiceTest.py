from elevenlabs.client import ElevenLabs
from elevenlabs import play, VoiceSettings

'''Access the EL api'''
client = ElevenLabs(
  api_key='secret-api-key',
)

'''Change Voice settings. '''
client.voices.edit_settings(
    voice_id="XfNU2rGpBa01ckF309OY",
    request=VoiceSettings(
        stability=0.33,
        similarity_boost=0.8,
        style=0.03,
    ),
)

'''Generate the audio'''
audio = client.generate(
  text="This is a test for both english and spanish voice. Hoy dia, todo esta bien. Enserio sera esto posible",
  voice = 'XfNU2rGpBa01ckF309OY',
  model = "eleven_multilingual_v2"
)

play(audio) 

