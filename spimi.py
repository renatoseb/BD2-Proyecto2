import math
import os
import numpy as np
from nltk.tokenize import word_tokenize
from collections import Counter
from .preprocessing import process

class Spimi:
    def _init_(self):
        self.document_count = 0
        self.token_count = 0
        self.matrix = None

    def build_index(self, documents):
        self.gen_matrix()
        self.norms = [np.linalg.norm(d) for d in self.matrix]

    def generate_file(self, tokens, document_id):
        self.document_count += 1
        self.term_count = len(tokens)

        for token in tokens:
            path = "indexes/"
            file = open(path + token + ".txt", "a+")
            
            file.seek(0)
            data = file.read(100)
            if len(data) > 0:
                file.write("\n")

            file.write(f'{document},{tokens[token]}')
            file.close()

    def cosine_similarity(self, a, b, norm_b):
        return np.dot(a, b) / (np.linalg.norm(a) * norm_b)

    def gen_matrix(self):
        directory = 'indexes'
        self.matrix = np.zeros((self.document_count, self.token_count))

        for i, filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                file = open(f)
                term_frequencies = file.readlines()
                # quantity of frequancies -> df
                idf = np.log((self.document_count + 1) / (len(term_frequencies) + 1)
                for tf in term_frequencies:
                    document_id = tf.split[0]
                    tfidf = tf.split[1] * idf
                    # TERMS NEED TO BE TRACKED BY SOME KIND OF ID
                    self.matrix[document_id][i] = tfidf

    def calculate_df(token):
        directory = "indexes/"
        f = directory + token + ".txt"
        if os.path.isfile(f):
            file = open(f)
            return len(file.readlines())


    def gen_vector(self, tokens):
        query = np.zeros(self.token_count)
        counter = counter(tokens)
        word_count = len(counter)

        for token in np.unique(tokens):
            tf = counter[token] / word_count
            idf = math.log((self.document_count + 1) / (calculate_df(token) + 1))
            
            #calculate term position on filesystem... XD

            directory = 'indexes'
            pos = 0
            for i, filename in os.listdir(directory):
                if filename == token + ".txt"
                    pos = i
                    break
            try:
                query[pos] = tf * idf
            except:
                pass
        return query
                
    def search(self, k, query):
        processed_query = process(query)
        tokens = word_tokenize(str(processed_query))

        cosines = []
        query_vector = self.gen_vector(tokens)

        idx = 0
        for vector in self.matrix:
            cosines.append(self.cosine_similarity(query_vector, vector, self.norms[idx]))
            idx += 1

        out = np.array(cosines).argsort()[-k:][::-1]
        doc_ids = [number for number in out]
        return doc_ids



