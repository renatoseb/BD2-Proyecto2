import pandas as pd
from preprocessing import procesamiento

header = ["title","publication","author","year","content"]
csv_data = pd.read_csv('datasets/articles1.csv', usecols = header)


print(list(csv_data.loc[:, 0]))