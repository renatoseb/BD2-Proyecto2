import sqlalchemy as sa
from sqlalchemy_utils import database_exists, create_database
import json, os
import nltk
nltk.download('stopwords')

# Reading credentials
f = open('credentials.json')
credentials = json.load(f)
db_user = credentials['username']
db_pass = credentials['password']


uri = f'postgresql://{db_user}:{db_pass}@localhost:5432/allthenews'

engine = sa.create_engine(uri, echo=True)

if not database_exists(engine.url):
    print("Creating database...")
    create_database(engine.url)

with engine.connect().execution_options(autocommit=True) as con:
    result = con.execute(sa.sql.text("""
            CREATE TABLE IF NOT EXISTS news (
                n INTEGER,
                id integer PRIMARY KEY, 
                title text,
                publication text,
                author text,
                date text,
                year text, 
                month text, 
                url text, 
                content text
            );

            alter table news add column content_ts tsvector;

            create index idx_content_ts on news using gin (content_ts);
    """))
    print("Creating database IF NOT EXISTS...")
    print(result)
    

    path_base = os.path.dirname(os.getcwd())
    path_dataset_1 = os.path.join(path_base, "datasets", "articles1.csv")
    print("Inserting articles1.csv...")
    result = con.execute(sa.sql.text(f"""
            COPY news(n, id, title, publication, author, date, year, month, url, content)
            FROM '{path_dataset_1}'
            DELIMITER ','
            CSV HEADER;
    """))
    print(result)

    path_dataset_2 = os.path.join(path_base, "datasets", "articles2.csv")
    print("Inserting articles2.csv...")
    result = con.execute(sa.sql.text(f"""
            COPY news(n, id, title, publication, author, date, year, month, url, content)
            FROM '{path_dataset_2}'
            DELIMITER ','
            CSV HEADER;
    """))
    print(result)

    path_dataset_3 = os.path.join(path_base, "datasets", "articles3.csv")
    print("Inserting articles3.csv...")
    result = con.execute(sa.sql.text(f"""
            COPY news(n, id, title, publication, author, date, year, month, url, content)
            FROM '{path_dataset_3}'
            DELIMITER ','
            CSV HEADER;
    """))
    print(result)

    print("FILLING FIELD TO QUERIES...")
    result = con.execute(sa.sql.text("""
            update news
            set content_ts = x.content_ts
            from (
            select Id, 
                    setweight(to_tsvector('english', title), 'A') ||
                    setweight(to_tsvector('english', content), 'B')
                    as content_ts
            from news
            ) as x
            where x.Id = news.Id;
    """))
    print(result)