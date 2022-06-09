import nltk
import numpy as np

from num2words import num2words
from collections import Counter

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english')


def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}’”“—'~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
    data = np.char.replace(data, ',', '')
    #data = np.char.replace(data, "'", '')
    return str(data)

def numbers_to_text(data):
    tokens = nltk.word_tokenize(str(data))
    new_txt = ''
    for w in tokens:
        try:
            w = num2words(int(w))
        except Exception as e:
            pass
        new_txt = f'{new_txt} {w}'
    new_txt = np.char.replace(new_txt, '-', '')
    return str(new_txt)


def process(texto):
    #MUST DOWNLOAD FIRST
    #nltk.download('stopwords')
    texto = texto.lower()

    texto = remove_punctuation(texto)
    texto = numbers_to_text(texto)

    texto_token = nltk.word_tokenize(texto)
    stop_words = stopwords.words('english')

    texto_tokens_c = texto_token[:]
    for token in texto_token:
        if token in stop_words:
            texto_tokens_c.remove(token)

    texto_token_s = []
    for w in texto_tokens_c:
        texto_token_s.append(stemmer.stem(w))
    
    
    return Counter(texto_token_s)
