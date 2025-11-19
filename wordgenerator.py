from deep_translator import (GoogleTranslator as GT,
                             single_detection,
                             batch_detection)
from wonderwords import RandomSentence as RS


def any_sentence(text):
     text = RS()
     texto = text.sentence()
     return texto


def translate(text):
     text_translated = GT(source = "auto", target = "de").translate(text)
     print(text_translated)
     return text_translated
    
texto = ''
text = any_sentence(texto)
print(text)
translate(text)