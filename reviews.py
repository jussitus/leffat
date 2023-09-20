from db import db
from sqlalchemy.sql import text


def get_movie_reviews(id):
    sql = text("""SELECT users.user_username, reviews.review_user_id, reviews.review_date, 
                  reviews.review_text, reviews.review_score 
                  FROM reviews, users 
                  WHERE reviews.review_movie_id=:id AND reviews.review_user_id=users.user_id""")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_average_score(id):
    sql = text("""SELECT AVG(review_score) FROM reviews WHERE review_movie_id=:id""")
    result = db.session.execute(sql, {"id":id})
    return round(result.fetchone()[0], 2)