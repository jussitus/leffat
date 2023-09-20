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

def add_review(user_id, movie_id, review_text, review_score):
    try:
        sql = text("""INSERT INTO reviews (review_user_id, review_movie_id, review_date, review_text, review_score) 
                    VALUES (:user_id, :movie_id, NOW(), :review_text, :review_score)""")
        db.session.execute(sql, {"user_id":user_id, "movie_id":movie_id, "review_text":review_text, "review_score":review_score})
        db.session.commit()
        return True
    except:
        return False