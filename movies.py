from sqlalchemy.sql import text
from db import db

def get_movies():
    sql = text(
        """
            SELECT
                movie_id,
                movie_name,
                movie_year
            FROM 
                movies 
            ORDER BY
                movie_name
        """
    )
    result = db.session.execute(sql)
    return result.fetchall()


def get_movie(movie_id):
    sql = text(
        """
            SELECT
                movie_id,
                movie_name,
                movie_year 
            FROM
                movies 
            WHERE 
                movie_id=:movie_id
        """
    )
    result = db.session.execute(sql, {"movie_id": movie_id})
    return result.fetchone()


def add_movie(movie_name, movie_year, movie_runtime):
    try:
        sql = text(
            """
                INSERT INTO movies 
                    (
                        movie_name,
                        movie_year,
                        movie_runtime
                    )
                VALUES 
                    (
                        :movie_name,
                        :movie_year,
                        :movie_runtime
                    )
            """
        )
        db.session.execute(sql, {"movie_name": movie_name, "movie_year": movie_year, "movie_runtime":movie_runtime})
        db.session.commit()
        return True
    except:
        return False


def get_reviews(movie_id):
    sql = text(
        """
            SELECT 
                users.user_username,
                reviews.review_user_id,
                reviews.review_date, 
                reviews.review_text, 
                reviews.review_score 
            FROM
                users,
                reviews
            WHERE 
                reviews.review_movie_id=:movie_id 
            AND
                reviews.review_user_id=users.user_id
        """
    )
    result = db.session.execute(sql, {"movie_id": movie_id})
    return result.fetchall()
