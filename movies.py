from db import db
from sqlalchemy.sql import text


def get_movies():
    sql = text("SELECT movie_id, movie_name, movie_year FROM movies ORDER BY movie_name")
    result = db.session.execute(sql)
    return result.fetchall()

def get_movie(id):
    sql = text("SELECT movie_id, movie_name, movie_year FROM movies WHERE movie_id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()