import logging
import os

import speech_recognition as sr


def show_microphones():
    audio_sources = sr.Microphone.list_microphone_names()
    print('-'*15)
    for index, name in enumerate(audio_sources):
        print(f'Index: "{index}" = `Microphone(device_index={name})`')
    print('-'*15)

def get_microphone():
    audio_sources = sr.Microphone.list_microphone_names()
    for index, name in enumerate(audio_sources):
        if 'microphone' in name.lower():
            logging.info(f'[Found] {name})')
            return index
    raise ValueError('No microphone detected')    


def transcribe(device_index=None, language='en-US'):
    if device_index is None:
        error_msg = ('Set Microphone try\n'
            '>>> device_index = get_microphone()\n'
            '>>> transcribe(device_index=device_index)\n'
        )
        raise ValueError(error_msg)

    #device_index= get_microphone()
    r = sr.Recognizer()
    with sr.Microphone(device_index=device_index) as source:
        # listen for 1 sec to calibrate the energy threshold
        # for ambient noise levels 
        r.adjust_for_ambient_noise(source)
        print('Speaker: ', end='', flush=True)
        audio = r.listen(source)

    # set up the response object
    response = {
        'success': False,
        'error': None,
        'transcribed': None
    } 

    # Try catch the voice
    try:
        response['transcribed'] = r.recognize_google(
            audio, language=language, key=os.environ.get('GOOGLESTTAPI'))
        response['success'] = True
    except sr.UnknownValueError:
        response['error'] = 'Could not understand audio'
        logging.error('Audio Problems', exc_info=True)
    except sr.RequestError:
        response['error'] = 'API Issues. Connection Failure'
        logging.error('API Problems', exc_info=True)   
    return response
