from vtt import VoiceToText



response = VoiceToText.transcribe(audio_in='data/audios/try3.wav', language='en-US')

if response.get('success'):
    text = response.get('transcribed')
else:
    # print(response.get('error'))
    text = None

print(text)
