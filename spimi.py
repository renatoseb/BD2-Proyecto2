def spimi(tokens, document):
    token_dictionary = {}

    
    for token in tokens:
        path = "indexes/"
        file = open(path + token + ".txt", "a+")
        
        file.seek(0)
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")

        file.write(f'{document},{tokens[token]}')
        file.close()

"""
    with open(file_name, "a+") as file_object:
        
        
            file.seek(0)
            data = file.read(100)
            if len(data) > 0:
                file_object.write("\n")

        for i, key in enumerate(tokens):
            file_object.write(key+"\n")"""