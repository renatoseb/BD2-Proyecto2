import os
import math
from preprocessing import process

N = 50_000

def search(Q, k = 5):
        query = process(Q)
        query_length = 0
        documents = {}
        directory = "indexes/"
        query_answer = []

        for term in query:
                path = directory + term + ".txt"
                
                if not os.path.isfile(path):
                        pass

                file = open(path)
                df = 0

                for line in file.readlines():
                        #document, tf = line.split(",")
                        line = line.split(",")

                        document = line[0]
                        tf = line[1]
                        title = line[2:]
                        title = ''.join(title).rstrip()

                        prev = []
                        if (document, title) in documents:
                                prev = documents[(document, title)]
                        documents[(document, title)] = prev + [(term, math.log(1 + int(tf)))]
                        df += 1

                w = math.log(1 + query[term]) * math.log(1 + N /df)
                query_length += w ** 2
                query[term] = w
        
        query_length = query_length ** (1 / 2)

        for term in query:
                query[term] = 1 / query_length

        for document, title in documents:
                ranking = 0
                document_length = 0
                document_vector = documents[(document, title)]

                for term, w in document_vector:
                        document_length += w ** 2
                document_length = w ** (1/2)

                for term, w in document_vector:
                        ranking += query[term] * w / document_length

                query_answer.append((title, ranking))

        query_answer = sorted(query_answer, key = lambda x: x[1])
        return query_answer

q = input()

print(search(q, 10))