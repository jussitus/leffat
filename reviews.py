from sqlalchemy.sql import text
from db import db


def get_average_score(movie_id):
    sql = text(
        "SELECT ROUND(AVG(review_score),2) FROM reviews WHERE review_movie_id=:movie_id"
    )
    result = db.session.execute(sql, {"movie_id": movie_id})
    return result.fetchone()[0]


def add_review(user_id, movie_id, review_text, review_score):
    try:
        sql = text(
            "INSERT INTO reviews (review_user_id, review_movie_id, "
            "review_date, review_text, review_score) "
            "VALUES(:user_id, :movie_id, NOW(), :review_text, :review_score) "
        )
        db.session.execute(
            sql,
            {
                "user_id": user_id,
                "movie_id": movie_id,
                "review_text": review_text,
                "review_score": review_score,
            },
        )
        db.session.commit()
        return True
    except:
        return False


def remove_review(review_id):
    try:
        sql = text("DELETE FROM reviews WHERE review_id=:review_id")
        db.session.execute(sql, {"review_id": review_id})
        db.session.commit()
        return True
    except:
        return False
