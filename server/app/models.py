from app import db
import requests
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

def fetch_and_store_tmdb_data():
    API_KEY = "e407ef47003f178633c02269142f8b86"
    BASE_URL = "https://api.themoviedb.org/3"
    
    # Fetch Movies
    movies_endpoint = f"{BASE_URL}/movie/now_playing?api_key={API_KEY}"
    movies_response = requests.get(movies_endpoint)
    if movies_response.status_code == 200:
        movies_data = movies_response.json()
        for movie in movies_data["results"]:
            existing_movie = Movie.query.filter_by(tmdb_id=movie["id"]).first()
            if existing_movie:
                continue
            new_movie = Movie(
                tmdb_id=movie["id"],
                title=movie["title"],
                overview=movie["overview"],
                release_date=datetime.strptime(movie["release_date"], "%Y-%m-%d").date(),
                poster_path=movie["poster_path"]
            )
            db.session.add(new_movie)
    else:
        print(f"Error fetching movies data from TMDB: {movies_response.status_code}")

    # Fetch TV Shows
    tv_shows_endpoint = f"{BASE_URL}/tv/on_the_air?api_key={API_KEY}"
    tv_shows_response = requests.get(tv_shows_endpoint)
    if tv_shows_response.status_code == 200:
        tv_shows_data = tv_shows_response.json()
        for tv_show in tv_shows_data["results"]:
            existing_tv_show = TVShow.query.filter_by(tmdb_id=tv_show["id"]).first()
            if existing_tv_show:
                continue
            new_tv_show = TVShow(
                tmdb_id=tv_show["id"],
                name=tv_show["name"],
                overview=tv_show["overview"],
                first_air_date=datetime.strptime(tv_show["first_air_date"], "%Y-%m-%d").date(),
                poster_path=tv_show["poster_path"]
            )
            db.session.add(new_tv_show)
    else:
        print(f"Error fetching TV shows data from TMDB: {tv_shows_response.status_code}")
    db.session.commit()

user_clubs = db.Table('user_clubs',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('club_id', db.Integer, db.ForeignKey('clubs.id'), primary_key=True)
)

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users.id'))
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    profile_pic = db.Column(db.String(200))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    posts = db.relationship('Post', back_populates='author', lazy='dynamic')
    comments = db.relationship('Comment', back_populates='author', lazy='dynamic')
    ratings = db.relationship('Rating', back_populates='author', lazy='dynamic')
    clubs = db.relationship('Club', secondary=user_clubs, back_populates='members')
    watched_movies = db.relationship('WatchedMovie', back_populates='user')
    
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    overview = db.Column(db.Text)
    release_date = db.Column(db.Date)
    poster_path = db.Column(db.String(200))

    posts = db.relationship('Post', back_populates='movie', lazy='dynamic')
    watched_by = db.relationship('WatchedMovie', back_populates='movie')

class TVShow(db.Model):
    __tablename__ = 'tv_shows'
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    overview = db.Column(db.Text)
    first_air_date = db.Column(db.Date)
    poster_path = db.Column(db.String(200))

    posts = db.relationship('Post', back_populates='tv_show', lazy='dynamic')

class Club(db.Model):
    __tablename__ = 'clubs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    genre = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    created_by = db.relationship('User', backref='created_clubs')
    members = db.relationship('User', secondary=user_clubs, back_populates='clubs')
    posts = db.relationship('Post', back_populates='club', lazy='dynamic')

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    tv_show_id = db.Column(db.Integer, db.ForeignKey('tv_shows.id'))
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'), nullable=False)

    author = db.relationship('User', back_populates='posts')
    movie = db.relationship('Movie', back_populates='posts')
    tv_show = db.relationship('TVShow', back_populates='posts')
    club = db.relationship('Club', back_populates='posts')
    comments = db.relationship('Comment', back_populates='post', lazy='dynamic')
    ratings = db.relationship('Rating', back_populates='post', lazy='dynamic')

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    author = db.relationship('User', back_populates='comments')
    post = db.relationship('Post', back_populates='comments')

class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    author = db.relationship('User', back_populates='ratings')
    post = db.relationship('Post', back_populates='ratings')

class WatchedMovie(db.Model):
    __tablename__ = 'watched_movies'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    watched_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', back_populates='watched_movies')
    movie = db.relationship('Movie', back_populates='watched_by')
