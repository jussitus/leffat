CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_username TEXT NOT NULL UNIQUE,
    user_password TEXT,
    user_isadmin BOOLEAN
);
CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    movie_name TEXT NOT NULL UNIQUE,
    movie_year INTEGER NOT NULL,
    movie_runtime INTEGER NOT NULL,
    CHECK (movie_year >= 1900 and movie_year <= 2099 and movie_runtime >= 1 and movie_runtime <= 2000)
);
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    review_user_id INTEGER REFERENCES users ON DELETE CASCADE,
    review_movie_id INTEGER REFERENCES movies ON DELETE CASCADE,
    review_date TIMESTAMP WITH TIME ZONE,
    review_text TEXT NOT NULL,
    review_score INTEGER NOT NULL,
    UNIQUE (review_user_id, review_movie_id),
    CHECK (review_score >= 1 AND review_score <= 5)
);
CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name TEXT NOT NULL UNIQUE
);
CREATE TABLE movies_genres (
    movies_genres_movie_id INTEGER REFERENCES movies ON DELETE CASCADE,
    movies_genres_genre_id INTEGER REFERENCES genres ON DELETE CASCADE,
    PRIMARY KEY (movies_genres_movie_id, movies_genres_genre_id)
);
CREATE TABLE directors (
    director_id SERIAL PRIMARY KEY,
    director_name TEXT NOT NULL UNIQUE
);
CREATE TABLE movies_directors (
    movies_directors_movie_id INTEGER REFERENCES movies ON DELETE CASCADE,
    movies_directors_director_id INTEGER REFERENCES directors ON DELETE CASCADE,
    PRIMARY KEY (movies_directors_movie_id, movies_directors_director_id)
);
