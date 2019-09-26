import sys
sys.path.insert(0, '..')

from collections import defaultdict

from fastapi import FastAPI
from vtt import VoiceToText

app = FastAPI(__file__)
storage = defaultdict(list)

@app.get('/')
def index():
    return {"Hello": "World"}

@app.post('/data')
async def send():

    while True:
        response = VoiceToText.transcribe(device_index=0, language='en-US')

        if response.get('success'):
            text = response.get('transcribed')

            storage['profile'].append('jack')
            storage['text'].append(text)
        else:
            # print(response.get('error'))
            text = None
            storage['profile'].append('Error')
            storage['text'].append(text)

        return {'data': dict(storage)}


if __name__ == '__main__':
    app.run(debug=True, threaded=True)