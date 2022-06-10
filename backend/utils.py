import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}’”“—'~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
    data = np.char.replace(data, ',', '')
    #data = np.char.replace(data, "'", '')
    return str(data)

def query_tokens(query):
    query = query.lower()
    query = remove_punctuation(query)
    # Tokenizando texto
    tokens_text = nltk.word_tokenize(query)

    # Importando stopwords
    stop_words = stopwords.words('english')

    # Quitando stopwords
    texto_tokens_c = tokens_text[:]
    for token in tokens_text:
        if token in stop_words:
            texto_tokens_c.remove(token)

    return texto_tokens_c