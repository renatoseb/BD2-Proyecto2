import pymongo


client = pymongo.MongoClient('localhost', 27017)
db = client.db2project
db.articles1.drop_index("prueba1")
db.articles1.create_index([('title', 'text'), ('content', 'text')], name="prueba1")

search = db.articles1.find(
    { "$text": { "$search": "washington post" } },
    { "score": { "$meta": "textScore" } }).limit(10)

search.sort([( "score", { "$meta": "textScore" } )])

i = 0
for x in search:
    print(x)
    print("______________________________________________________")
    if i == 9:
        break
    i += 1