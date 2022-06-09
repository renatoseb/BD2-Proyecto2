import nltk
from collections import Counter

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')

def procesamiento(texto):
    texto_token = nltk.word_tokenize(texto)
    with(open("stop.txt", encoding='UTF-8')) as file:
        stoplist = [line.lower().strip() for line in file]
    stoplist += [",", ".", "¿", "?"]

    texto_tokens_c = texto_token[:]
    for token in texto_token:
        if token.lower() in stoplist:
            texto_tokens_c.remove(token)

    texto_token_s = []
    for w in texto_tokens_c:
        texto_token_s.append(stemmer.stem(w))
    
    
    return Counter(texto_token_s)