"""
Pasos: 
- Descargar MongoDB con MongoDB Compass
- Establecer una conexión en el puerto predeterminado 27017
- Crear una nueva base de datos llamada db2project
- Dentro de la base de datos, crear la colección articles1
"""

import pymongo
import csv

csv.field_size_limit(100000000)

client = pymongo.MongoClient('localhost', 27017)
db = client.db2project
db.articles1.drop()


header = ["id", "title", "publication", "author", "date", "year", "month", "url", "content"]
for i in range(3):
    file_path = "articles"+str(i+1)+".csv"
    csvfile = open("../datasets/"+file_path, encoding="utf-8")
    reader = csv.DictReader(csvfile)

    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]
        
        db.articles1.insert_one(row)
