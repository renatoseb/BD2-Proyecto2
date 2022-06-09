"""
Pasos: 
- Descargar MongoDB con MongoDB Compass
- Establecer una conexión en el puerto predeterminado 27017
- Crear una nueva base de datos llamada db2project
- Dentro de la base de datos, crear las colecciones articles1, articles2 y articles3
"""

import pymongo
import csv

csv.field_size_limit(100000000)

client = pymongo.MongoClient('localhost', 27017)
db = client.db2project
db.articles1.drop()
db.articles2.drop()
db.articles3.drop()


header = ["id", "title", "publication", "author", "date", "year", "month", "url", "content"]
file_path1 = "articles1.csv"
file_path2 = "articles2.csv"
file_path3 = "articles3.csv"
csvfile1 = open("datasets/"+file_path1, encoding="utf-8")
csvfile2 = open("datasets/"+file_path2, encoding="utf-8")
csvfile3 = open("datasets/"+file_path3, encoding="utf-8")
reader1 = csv.DictReader(csvfile1)
reader2 = csv.DictReader(csvfile2)
reader3 = csv.DictReader(csvfile3)

for each in reader1:
    row = {}
    for field in header:
        row[field] = each[field]
    
    db.articles1.insert_one(row)
    
for each in reader2:    
    row = {}
    for field in header:
        row[field] = each[field]
        
    db.articles2.insert_one(row)

for each in reader3:
    row = {}
    for field in header:
        row[field] = each[field]

    db.articles3.insert_one(row)