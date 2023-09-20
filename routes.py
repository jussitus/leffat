from app import app
from flask import redirect, render_template, request, session, url_for
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

@app.route("/movie/<movie_id>", methods=["GET", "POST"])
def movie(movie_id):
    if request.method == "GET":
        movie = m.get_movie(movie_id)
        reviews = r.get_movie_reviews(movie_id)
        reviewed = any(session.get("id") == review.review_user_id for review in reviews)
        average_score = 0 if len(reviews) == 0 else r.get_average_score(movie_id)
        return render_template("movie.html", movie=movie, reviews=reviews, average_score=average_score, reviewed=reviewed)
    if request.method == "POST":
        user_id = session.get("id")
        review_text = request.form["review_text"]
        review_score = request.form["review_score"]
        r.add_review(user_id, movie_id, review_text, review_score)
        return redirect(url_for("movie", movie_id=movie_id))

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    u.login(username,password)
    return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        u.signup(username,password, False)
        return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
