def spimi(tokens, document, title):
    for token in tokens:
        path = "indexes/"
        file = open(path + token + ".txt", "a+")
        
        file.seek(0)
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")

        file.write(f'{document},{tokens[token]},{title}')
        file.close()