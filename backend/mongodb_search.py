import pymongo
import time
import nltk
from nltk.corpus import stopwords
from utils import query_tokens


client = pymongo.MongoClient('localhost', 27017)
db = client.db2project

# db.articles1.create_index([('title', 'text'), ('content', 'text')], name="content_ts")


def get_mongodb_topk(text, k):
    query = query_tokens(text)

    format_text = " ".join(query)

    start = time.time()

    search = db.articles1.find(
        { "$text": { "$search": format_text } },
        { "score": { "$meta": "textScore" } }).limit(k)

    search.sort([( "score", { "$meta": "textScore" } )])

    end = time.time()

    query_time = round(end - start, 6)

    data = []
    for row in search:
        curr = {}
        curr['title'] = row['title']
        curr['content'] = row['content']
        curr['score'] = row['score']
        data.append(curr)

    response = {"data": data, "time": query_time }

    return response