from elevenlabs.client import ElevenLabs
from elevenlabs import play, VoiceSettings

'''Access the EL api'''
client = ElevenLabs(
  api_key='sk_bd2588eedba7547c6fba9e9ca6eb3dd6a1b2911cbcd8e9f3',
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

