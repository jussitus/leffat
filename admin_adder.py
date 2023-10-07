from os import getenv
import os
import psycopg2
from werkzeug.security import generate_password_hash

with open(".env") as f:
    lines = f.readlines()
    for line in lines:
        if "DATABASE_URL" in line:
            env = line.split("=")
            os.environ["DATABASE_URL"] = env[1]
hash_value = generate_password_hash("admin")
db_url = getenv("DATABASE_URL").removeprefix("postgresql:///")
print(db_url)
conn = psycopg2.connect(f"dbname={db_url}")
cur = conn.cursor()
cur.execute(
    "INSERT INTO users (user_username, user_password, user_isadmin) VALUES (%s, %s, TRUE)",
    ("admin", hash_value),
)
conn.commit()
cur.close()
conn.close()
