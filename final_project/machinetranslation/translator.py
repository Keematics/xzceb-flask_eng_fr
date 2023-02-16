""" Language Translation Instance """
import os
# import json 
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """ English to French translation function """
    if len(english_text) == 0:
        french_text  = None
    else:
        result = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text  = result['translations'][0]['translation']
    return french_text

def french_to_english(french_text ):
    """ French to English translation function """
    if len(french_text ) == 0:
        english_text = None
    else:
        result = language_translator.translate(
            text=french_text ,
            model_id='fr-en').get_result()
        english_text = result['translations'][0]['translation']
    return english_text
