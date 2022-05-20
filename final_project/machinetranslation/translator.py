'''
Module contains french to english and english to french
translation functions
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def get_translator_instance():
    ''' get IBM translator service '''
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    return language_translator

def english_to_french(english_text):
    ''' translate english to french '''
    language_translator = get_translator_instance()

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    text_result = translation["translations"][0]["translation"]

    return text_result

def french_to_english(french_text):
    ''' translate french to english '''
    language_translator = get_translator_instance()

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    text_result = translation["translations"][0]["translation"]

    return text_result
