CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_username TEXT UNIQUE,
    user_password TEXT,
    user_isadmin BOOLEAN ON DELETE CASCADE
);
CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    movie_name TEXT UNIQUE,
    movie_year INTEGER
);
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    review_user_id INTEGER REFERENCES users,
    review_movie_id INTEGER REFERENCES movies,
    review_date TIMESTAMP WITH TIME ZONE,
    review_text TEXT,
    review_score INTEGER
);
CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name TEXT UNIQUE
);
CREATE TABLE movies_genres (
    movies_genres_movie_id INTEGER REFERENCES movies,
    movies_genres_genre_id INTEGER REFERENCES movies,
    PRIMARY KEY (movies_genres_movie_id, movies_genres_genre_id)
);
