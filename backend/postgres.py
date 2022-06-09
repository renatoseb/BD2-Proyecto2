import sqlalchemy as sa
import json

# Reading credentials
f = open('credentials.json')
credentials = json.load(f)
db_user = credentials['username']
db_pass = credentials['password']

uri = f'postgresql://{db_user}:{db_pass}@localhost:5432/allthenews'

engine = sa.create_engine(uri, echo=True)



    # print("Connected to database allthenews!")