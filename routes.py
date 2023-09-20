from app import app
from flask import redirect, render_template, request, session
import movies as m, users as u, reviews as r
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/movies")
def movies():
    movies = m.get_movies()
    return render_template("movies.html", movies=movies)

@app.route("/users")
def users():
    users = u.get_users()
    return render_template("users.html", users=users)

@app.route("/user/<user_id>")
def user(user_id):
    user = u.get_user(user_id)
    return render_template("user.html", user=user)

@app.route("/movie/<movie_id>")
def movie(movie_id):
     movie = m.get_movie(movie_id)
     reviews = r.get_movie_reviews(movie_id)
     average_score = r.get_average_score(movie_id)
     # MITEN SAAN NIMET??
     return render_template("movie.html", movie=movie, reviews=reviews, average_score=average_score)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
