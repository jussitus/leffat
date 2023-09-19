from app import app
from flask import render_template
import functions
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/movies")
def movies():
    movies = functions.get_movies()
    return render_template("movies.html", movies=movies)

@app.route("/users")
def users():
    users = functions.get_users()
    return render_template("users.html", users=users)

@app.route("/user/<username>")
def user(username):
    user = functions.get_user(username)
    return render_template("user.html", user=user)