from sqlalchemy.sql import text
from db import db


def get_movies(query):
    name = query.get("name", default="")
    min_year = query.get("min_year", default=1900)
    max_year = query.get("max_year", default=2099)
    min_runtime = query.get("min_runtime", default=1)
    max_runtime = query.get("max_runtime", default=2000)
    sort = query.get("sort", default="name")
    order = query.get("order", default="asc")

    sql = """
            SELECT
                movies.movie_id,
                movies.movie_name,
                movies.movie_year,
                movies.movie_runtime,
                AVG(reviews.review_score)
            FROM
                movies LEFT JOIN reviews
            ON
                movies.movie_id = reviews.review_movie_id
            WHERE
                LOWER(movies.movie_name) LIKE LOWER(:name)
                AND movies.movie_year >= :min_year
                AND movies.movie_year <= :max_year
                AND movies.movie_runtime >= :min_runtime
                AND movies.movie_runtime <= :max_runtime
            GROUP BY
                movies.movie_id
            ORDER BY
        """
    # sql injection opportunity ? :(
    if sort not in ["name", "year", "runtime", "score"] or order not in ["desc", "asc"]:
        raise ValueError
    if sort == "score":
        sql = sql + "\nAVG(reviews.review_score)" + " " + order + " NULLS LAST"
    else:
        sql = sql + "\nmovies.movie_" + sort + " " + order
    result = db.session.execute(
        text(sql),
        {
            "name": "%" + name + "%",
            "min_year": min_year,
            "max_year": max_year,
            "min_runtime": min_runtime,
            "max_runtime": max_runtime,
        },
    )
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
        db.session.execute(
            sql,
            {
                "movie_name": movie_name,
                "movie_year": movie_year,
                "movie_runtime": movie_runtime,
            },
        )
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
