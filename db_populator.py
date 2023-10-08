from os import getenv
import os
import psycopg2

with open(".env") as f:
    lines = f.readlines()
    for line in lines:
        if "DATABASE_URL" in line:
            env = line.split("=")
            os.environ["DATABASE_URL"] = env[1]
db_url = getenv("DATABASE_URL").removeprefix("postgresql:///")
conn = psycopg2.connect(f"dbname={db_url}")
cur = conn.cursor()
cur.execute(
    """ 
    INSERT INTO movies
        (movie_name, movie_year, movie_runtime)

    SELECT 
        LEFT(MD5(RANDOM()::TEXT), (FLOOR(RANDOM()*12+1))::INTEGER),
        FLOOR(1900 + 125*RANDOM()),
        FLOOR(1 + 300*RANDOM())  
    FROM
        GENERATE_SERIES(1,100000)
    ON CONFLICT DO NOTHING;
    """
)
conn.commit()
cur.close()
conn.close()
