from db import db
from sqlalchemy.sql import text

def get_user(id):
    sql = text("SELECT * FROM users WHERE user_id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def get_users():
    sql = text("SELECT user_id, user_username FROM users")
    result = db.session.execute(sql)
    return result.fetchall()