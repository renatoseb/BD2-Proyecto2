import sqlalchemy as sa
import time
import json
import nltk
from nltk.corpus import stopwords 
import numpy as np

# Reading credentials
f = open('credentials.json')
credentials = json.load(f)
db_user = credentials['username']
db_pass = credentials['password']

uri = f'postgresql://{db_user}:{db_pass}@localhost:5432/allthenews'

engine = sa.create_engine(uri, echo=True)


def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}’”“—'~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
    data = np.char.replace(data, ',', '')
    #data = np.char.replace(data, "'", '')
    return str(data)

def get_postgres_topk(text, k):
    text = text.lower()
    text = remove_punctuation(text)
    # Tokenizando texto
    tokens_text = nltk.word_tokenize(text)

    # Importando stopwords
    stop_words = stopwords.words('english')
    
    # Quitando stopwords
    texto_tokens_c = tokens_text[:]
    for token in tokens_text:
        if token in stop_words:
            texto_tokens_c.remove(token)

    format_text = " | ".join(texto_tokens_c)
    
    with engine.connect().execution_options(autocommit=True) as con:
        start = time.time()
        result = con.execute(sa.sql.text(f""" 
            select title, content, ts_rank_cd(content_ts, query_ts) as score
            from news, to_tsquery('english', '{format_text}') query_ts
            where query_ts @@ content_ts
            order by score desc 
            limit {k};
        """))
        end = time.time()
        query_time = round(end - start, 6)
        data = []
        for row in result:
            curr = {}
            curr['title'] = row['title']
            curr['content'] = row['content']
            curr['score'] = row['score']
            data.append(curr)

        response = { "data": data, "time": query_time } 

    return response
