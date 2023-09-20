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

def add_movie(movie_name, movie_year):
    try:
        sql = text("""INSERT INTO movies (movie_name, movie_year) VALUES (:movie_name, :movie_year)""")
        db.session.execute(sql, {"movie_name":movie_name, "movie_year":movie_year})
        db.session.commit()
        return True
    except:
        return False
    
def get_reviews(id):
    sql = text("""SELECT users.user_username, reviews.review_user_id, reviews.review_date, 
                  reviews.review_text, reviews.review_score 
                  FROM reviews, users 
                  WHERE reviews.review_movie_id=:id AND reviews.review_user_id=users.user_id""")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()