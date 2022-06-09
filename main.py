import pandas as pd
import csv
csv.field_size_limit(100000000)

from preprocessing import process
from spimi import spimi

#Parsing CSV to txt made by Eduardo
def parsing_to_txt():
    file_name = "articles1.csv"

    file = open("datasets/" + file_name, encoding='UTF-8')
    reader = csv.reader(file)
    next(reader)
    #i = 1
    for row in reader:
        new_file = open("datasets/input.txt", "+a")
        #new_file = open("datasets/input"+str(i)+".txt", "+a")
        new_file.write(row[9].rstrip())
        break



def run():
    file_name = "articles1.csv"

    file = open("datasets/" + file_name, encoding='UTF-8')
    documents = csv.reader(file)
    next(documents)

    index_documents = [1 ,3]

    for i, document in enumerate(documents):
        if i in index_documents:    
            tokens = process(document[9].rstrip())
            spimi(tokens, i)

        if i == 10:
            break
run()
