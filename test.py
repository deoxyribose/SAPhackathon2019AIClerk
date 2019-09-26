from vtt import vttapi

print('\n Voice to Text\n Setting microphone ...\n')

while True:
    response = vttapi.transcribe(device_index=0, language='en-US')

    if response.get('success'):
        text = response.get('transcribed')
    else:
        # print(response.get('error'))
        text = None
    print(text)

    print('\n\n')