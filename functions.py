from db import db
from sqlalchemy.sql import text

def get_movies():
    sql = text("SELECT movie_id, movie_name, movie_year FROM movies")
    result = db.session.execute(sql)
    return result.fetchall()


def get_users():
    sql = text("SELECT user_id, user_username FROM users")
    result = db.session.execute(sql)
    return result.fetchall()

def get_movie_reviews(id):
    sql = text("""SELECT review_user_id, review_date, review_text, review_score FROM reviews WHERE review_movie_id=:id""")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_movie(id):
    sql = text("SELECT movie_name, movie_year FROM movies WHERE movie_id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def get_user(id):
    sql = text("SELECT * FROM users WHERE user_id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()