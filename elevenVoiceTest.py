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
  text="Welcome to Datacamp's beginner's guide to the ElevenLabs API. Hoy dia, todo esta bien. Cuantos cuentos cuenta Pablo? Que tal diez?",
  voice = 'XfNU2rGpBa01ckF309OY',
  model = "eleven_multilingual_v2"
)

play(audio) 

