from db import db
from sqlalchemy.sql import text

def get_movies():
    sql = text("SELECT movie_name, movie_year FROM movies")
    result = db.session.execute(sql)
    return result.fetchall()


def get_users():
    sql = text("SELECT user_username FROM users")
    result = db.session.execute(sql)
    return result.fetchall()

def get_user(username):
    sql = text("SELECT user_username FROM users WHERE user_username=:username")
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()