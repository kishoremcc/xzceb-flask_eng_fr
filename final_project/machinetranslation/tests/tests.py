import unittest
from ibm_watson import ApiException
from translator import translation
#from translator import english_to_french, french_to_english
class TestMyLanguageTranslator(unittest.TestCase):

    def setUp(self):
        self.translator = translation ()

    def test_translate_english_to_french(self):
        text = 'Hello'
        expected_translation = 'Bonjour?'
        try:
            result = self.translator.translate(text, 'en-es')
            self.assertEqual(result, expected_translation)
        except ApiException as ex:
            self.fail(f"Translation failed: {ex}")

    def test_translate_french_to_english(self):
        text = 'Bonjour'
        expected_translation = 'Hello?'
        try:
            result = self.translator.translate(text, 'es-en')
            self.assertEqual(result, expected_translation)
        except ApiException as ex:
            self.fail(f"Translation failed: {ex}")