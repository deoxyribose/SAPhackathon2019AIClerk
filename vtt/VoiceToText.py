import logging
import os

import speech_recognition as sr


def transcribe(audio_in=None, language='en-US'):
    
    r = sr.Recognizer()
    with sr.AudioFile(audio_in) as source:
        audio = r.record(source) 

    # set up the response object
    response = {
        'success': False,
        'error': None,
        'transcribed': None
    } 

    # Try catch the voice
    try:
        response['transcribed'] = r.recognize_google(
            audio, language=language, key=None) # Here goes API Keys
        response['success'] = True
    except sr.UnknownValueError:
        response['error'] = 'Could not understand audio'
        logging.error('Audio Problems', exc_info=True)
    except sr.RequestError:
        response['error'] = 'API Issues. Connection Failure'
        logging.error('API Problems', exc_info=True)   
    return response
