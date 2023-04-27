import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('wVnM0eRR9OXlvlSKd_rOmkueZLSqaRsZSG07bmI93wSq')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/66e45c46-6fc8-4b02-9b1d-f620651ead0a')

translation = language_translator.translate(
    text='Hello?',
    model_id='en-fr').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

translation = language_translator.translate(
    text='Bonjour?',
    model_id='fr-en').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))