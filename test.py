from vtt import VoiceToText

print('\n Voice to Text\n Setting microphone ...\n')

while True:
    response = VoiceToText.transcribe(device_index=0, language='en-US')

    if response.get('success'):
        text = response.get('transcribed')
    else:
        # print(response.get('error'))
        text = None
    print(text)

    if 'quit' in text.split():
        print('Good bye')
        break

    print('\n\n')