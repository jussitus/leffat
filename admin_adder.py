import psycopg2
from werkzeug.security import generate_password_hash


hash_value = generate_password_hash("admin")
conn = psycopg2.connect("dbname=leffatus_db")
cur = conn.cursor()
cur.execute(
    "INSERT INTO users (user_username, user_password, user_isadmin) VALUES (%s, %s, TRUE)",
    ("admin", hash_value),
)
conn.commit()
cur.close()
conn.close()
