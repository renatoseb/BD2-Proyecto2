import sqlalchemy as sa
import time
import json
from utils import query_tokens

# Reading credentials
f = open('credentials.json')
credentials = json.load(f)
db_user = credentials['username']
db_pass = credentials['password']

uri = f'postgresql://{db_user}:{db_pass}@localhost:5432/allthenews'

engine = sa.create_engine(uri, echo=True)


def get_postgres_topk(text, k):
    query = query_tokens(text)

    format_text = " | ".join(query)

    with engine.connect().execution_options(autocommit=True) as con:
        start = time.time()
        result = con.execute(sa.sql.text(f""" 
            select title, publication, author,ts_rank_cd(content_ts, query_ts) as score
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
            curr['publication'] = row['publication']
            curr['author'] = row['author']
            curr['score'] = row['score']
            data.append(curr)

        response = { "data": data, "time": query_time } 

    return response
