from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()

MOVIE_DB_API_KEY = os.environ['API_KEY']
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500/"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Film(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateFilmForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddFilmForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    result = db.session.execute(db.select(Film).order_by(Film.rating.desc()))
    all_films = result.scalars().all()
    rank = 1
    for film in all_films:
        film.ranking = rank
        rank += 1
    db.session.commit()

    return render_template("index.html", films=all_films)

@app.route("/edit", methods=["GET", "POST"])
def rate_film():
    form = RateFilmForm()
    film_id = request.args.get("id")
    film = db.get_or_404(Film, film_id)
    if form.validate_on_submit():
        film.rating = float(form.rating.data)
        film.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", film=film, form=form)

@app.route("/delete")
def delete_film():
    film_id = request.args.get("id")
    film = db.get_or_404(Film, film_id)
    db.session.delete(film)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        film_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query":film_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find_film():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Film(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            rating=0,
            ranking=data["popularity"],
            review="To be completed.",
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("rate_film", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
