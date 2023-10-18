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
    page = query.get("page", default=0)
    genre = query.get("genre", default="")

    if_genre_from = ", movies_genres, genres" if genre else ""
    if_genre_where = (
        "AND movie_id = movies_genres_movie_id AND movies_genres_genre_id = genre_id AND genre_name = :genre"
        if genre
        else ""
    )

    sql = (
        "SELECT COUNT(movies.movie_id), movies.movie_id, movies.movie_name, "
        "movies.movie_year, movies.movie_runtime, AVG(reviews.review_score) "
        "FROM movies LEFT JOIN reviews ON movies.movie_id = reviews.review_movie_id "
        f"{if_genre_from} "
        "WHERE LOWER(movies.movie_name) LIKE LOWER(:name) AND movies.movie_year >= :min_year "
        "AND movies.movie_year <= :max_year AND movies.movie_runtime >= :min_runtime "
        "AND movies.movie_runtime <= :max_runtime "
        f"{if_genre_where} "
        "GROUP BY movies.movie_id "
        "ORDER BY "
    )
    if sort not in ["name", "year", "runtime", "score"] or order not in ["desc", "asc"]:
        raise ValueError
    if sort == "score":
        sql += "AVG(reviews.review_score) " + order + " NULLS LAST"
    else:
        sql += "\nmovies.movie_" + sort + " " + order
    # ITEMS PER PAGE 1/2
    sql += " LIMIT 100 OFFSET :page"
    result = db.session.execute(
        text(sql),
        {
            "name": "%" + name + "%",
            "min_year": min_year,
            "max_year": max_year,
            "min_runtime": min_runtime,
            "max_runtime": max_runtime,
            # ITEMS PER PAGE 2/2
            "page": int(page) * 100,
            "genre": genre,
        },
    )
    return result.fetchall()


def get_movie_count(query):
    name = query.get("name", default="")
    min_year = query.get("min_year", default=1900)
    max_year = query.get("max_year", default=2099)
    min_runtime = query.get("min_runtime", default=1)
    max_runtime = query.get("max_runtime", default=2000)
    genre = query.get("genre", default="")

    if_genre_from = ", movies_genres, genres" if genre else ""
    if_genre_where = (
        "AND movie_id = movies_genres_movie_id AND movies_genres_genre_id = genre_id AND genre_name = :genre"
        if genre
        else ""
    )

    sql = text(
        "SELECT COUNT(movie_id) "
        "FROM movies "
        f"{if_genre_from} "
        "WHERE LOWER(movie_name) LIKE LOWER(:name) AND movie_year >= :min_year "
        "AND movie_year <= :max_year AND movie_runtime >= :min_runtime "
        "AND movie_runtime <= :max_runtime "
        f"{if_genre_where}"
    )
    result = db.session.execute(
        sql,
        {
            "name": "%" + name + "%",
            "min_year": min_year,
            "max_year": max_year,
            "min_runtime": min_runtime,
            "max_runtime": max_runtime,
            "genre": genre,
        },
    )
    return result.fetchone()[0] // 100


def get_movie(movie_id):
    sql = text(
        "SELECT movie_id, movie_name, movie_year, movie_runtime "
        "FROM movies "
        "WHERE movie_id=:movie_id "
    )
    result = db.session.execute(sql, {"movie_id": movie_id})
    return result.fetchone()


def add_movie(movie_name, movie_year, movie_runtime):
    try:
        sql = text(
            "INSERT INTO movies (movie_name, movie_year, movie_runtime) "
            "VALUES (:movie_name, :movie_year, :movie_runtime) "
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
        "SELECT users.user_username, reviews.review_id, reviews.review_user_id, "
        "reviews.review_date, reviews.review_text, reviews.review_score "
        "FROM users, reviews "
        "WHERE reviews.review_movie_id=:movie_id "
        "AND reviews.review_user_id=users.user_id "
    )
    result = db.session.execute(sql, {"movie_id": movie_id})
    return result.fetchall()


def remove_movie(movie_id):
    try:
        sql = text("DELETE FROM movies WHERE movie_id=:movie_id")
        db.session.execute(sql, {"movie_id": movie_id})
        db.session.commit()
        return True
    except:
        return False


def add_genre(genre_name):
    try:
        sql = text("INSERT INTO genres (genre_name) VALUES (INITCAP(:genre_name))")
        db.session.execute(sql, {"genre_name": genre_name})
        db.session.commit()
        return True
    except:
        return False


def get_genres():
    sql = text("SELECT genre_id, genre_name FROM genres ORDER BY genre_name")
    result = db.session.execute(sql)
    return result.fetchall()


def add_movie_to_genre(genre_id, movie_id):
    try:
        sql = text(
            "INSERT INTO movies_genres (movies_genres_movie_id, movies_genres_genre_id) "
            "VALUES (:movie_id, :genre_id) "
        )
        db.session.execute(sql, {"genre_id": genre_id, "movie_id": movie_id})
        db.session.commit()
        return True
    except:
        return False


def get_movies_by_genre(genre_id):
    sql = text(
        "SELECT movie_id, movie_name "
        "FROM movies, movies_genres "
        "WHERE movies_genres_genre_id=:genre_id, movies_genres_movie_id=movie_id "
    )
    result = db.session.execute(sql, {"genre_id": genre_id})
    return result.fetchall()


def get_genres_by_movie(movie_id):
    sql = text(
        "SELECT genre_id, genre_name "
        "FROM genres, movies_genres "
        "WHERE movies_genres_movie_id=:movie_id and movies_genres_genre_id=genre_id "
        "ORDER BY genre_name "
    )
    result = db.session.execute(sql, {"movie_id": movie_id})
    return result.fetchall()
