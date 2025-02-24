from flask import request, jsonify, session, current_app as app
from app.models import db, User, Movie, TVShow, Club, Post, Comment, Rating, WatchedMovie
from functools import wraps
import requests
import logging
from datetime import datetime

# Error logging configuration
logging.basicConfig(level=logging.ERROR)

def get_tmdb_url(endpoint: str) -> str:
    return f"{app.config['TMDB_BASE_URL']}/{endpoint}"

@app.route('/discover/movies', methods=['GET'])
def discover_movies():
    try:
        endpoint = get_tmdb_url('discover/movie')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US",
            "page": 1
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "results" in data:
            movies = [
                {
                    "id": movie["id"],
                    "title": movie["title"],
                    "overview": movie["overview"],
                    "release_date": movie["release_date"],
                    "poster_path": movie["poster_path"]
                }
                for movie in data["results"]
            ]
            return jsonify(movies), 200
        else:
            logging.error(f"TMDB API response does not contain 'results' key: {data}")
            return jsonify({"error": "Failed to fetch movies"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching movies from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch movies"}), 500

@app.route('/discover/tv', methods=['GET'])
def discover_tv_shows():
    try:
        endpoint = get_tmdb_url('discover/tv')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US",
            "page": 1
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "results" in data:
            tv_shows = [
                {
                    "id": show["id"],
                    "name": show["name"],
                    "overview": show["overview"],
                    "first_air_date": show["first_air_date"],
                    "poster_path": show["poster_path"]
                }
                for show in data["results"]
            ]
            return jsonify(tv_shows), 200
        else:
            logging.error(f"TMDB API response does not contain 'results' key: {data}")
            return jsonify({"error": "Failed to fetch TV shows"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching TV shows from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch TV shows"}), 500

@app.route('/find/<int:tmdb_id>', methods=['GET'])
def find_by_id(tmdb_id):
    try:
        endpoint = get_tmdb_url(f'find/{tmdb_id}')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US",
            "external_source": "imdb_id"
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "movie_results" in data or "tv_results" in data:
            result = {
                "id": data["movie_results"][0]["id"] if data["movie_results"] else data["tv_results"][0]["id"],
                "title": data["movie_results"][0]["title"] if data["movie_results"] else data["tv_results"][0]["name"],
                "overview": data["movie_results"][0]["overview"] if data["movie_results"] else data["tv_results"][0]["overview"],
                "release_date": data["movie_results"][0]["release_date"] if data["movie_results"] else data["tv_results"][0]["first_air_date"],
                "poster_path": data["movie_results"][0]["poster_path"] if data["movie_results"] else data["tv_results"][0]["poster_path"]
            }
            return jsonify(result), 200
        else:
            logging.error(f"TMDB API response does not contain 'movie_results' or 'tv_results' key: {data}")
            return jsonify({"error": "Failed to find item by ID"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error finding item by ID from TMDB API: {e}")
        return jsonify({"error": "Failed to find item by ID"}), 500

@app.route('/genres/movies', methods=['GET'])
def get_movie_genres():
    try:
        endpoint = get_tmdb_url('genre/movie/list')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US"
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "genres" in data:
            genres = [{"id": genre["id"], "name": genre["name"]} for genre in data["genres"]]
            return jsonify(genres), 200
        else:
            logging.error(f"TMDB API response does not contain 'genres' key: {data}")
            return jsonify({"error": "Failed to fetch movie genres"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching movie genres from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch movie genres"}), 500

@app.route('/genres/tv', methods=['GET'])
def get_tv_genres():
    try:
        endpoint = get_tmdb_url('genre/tv/list')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US"
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "genres" in data:
            genres = [{"id": genre["id"], "name": genre["name"]} for genre in data["genres"]]
            return jsonify(genres), 200
        else:
            logging.error(f"TMDB API response does not contain 'genres' key: {data}")
            return jsonify({"error": "Failed to fetch TV genres"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching TV genres from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch TV genres"}), 500

@app.route('/guest-session/rated/movies', methods=['GET'])
def get_rated_movies():
    try:
        endpoint = get_tmdb_url('guest_session/new/rated/movies')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US"
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "results" in data:
            rated_movies = [
                {
                    "id": movie["id"],
                    "title": movie["title"],
                    "rating": movie["rating"]
                }
                for movie in data["results"]
            ]
            return jsonify(rated_movies), 200
        else:
            logging.error(f"TMDB API response does not contain 'results' key: {data}")
            return jsonify({"error": "Failed to fetch rated movies"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching rated movies from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch rated movies"}), 500

@app.route('/guest-session/rated/tv', methods=['GET'])
def get_rated_tv_shows():
    try:
        endpoint = get_tmdb_url('guest_session/new/rated/tv')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US"
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "results" in data:
            rated_tv_shows = [
                {
                    "id": show["id"],
                    "name": show["name"],
                    "rating": show["rating"]
                }
                for show in data["results"]
            ]
            return jsonify(rated_tv_shows), 200
        else:
            logging.error(f"TMDB API response does not contain 'results' key: {data}")
            return jsonify({"error": "Failed to fetch rated TV shows"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching rated TV shows from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch rated TV shows"}), 500

@app.route('/guest-session/rated/tv-episodes', methods=['GET'])
def get_rated_tv_episodes():
    try:
        endpoint = get_tmdb_url('guest_session/new/rated/tv/episodes')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US"
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "results" in data:
            rated_tv_episodes = [
                {
                    "id": episode["id"],
                    "name": episode["name"],
                    "rating": episode["rating"]
                }
                for episode in data["results"]
            ]
            return jsonify(rated_tv_episodes), 200
        else:
            logging.error(f"TMDB API response does not contain 'results' key: {data}")
            return jsonify({"error": "Failed to fetch rated TV episodes"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching rated TV episodes from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch rated TV episodes"}), 500

@app.route('/keywords/<int:keyword_id>', methods=['GET'])
def get_keyword_details(keyword_id):
    try:
        endpoint = get_tmdb_url(f'keyword/{keyword_id}')
        params = {
            "api_key": app.config['TMDB_API_KEY']
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        return jsonify(data), 200
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching keyword details from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch keyword details"}), 500

@app.route('/keywords/<int:keyword_id>/movies', methods=['GET'])
def get_movies_by_keyword(keyword_id):
    try:
        endpoint = get_tmdb_url(f'keyword/{keyword_id}/movies')
        params = {
            "api_key": app.config['TMDB_API_KEY'],
            "language": "en-US",
            "include_adult": False
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if "results" in data:
            movies = [
                {
                    "id": movie["id"],
                    "title": movie["title"],
                    "overview": movie["overview"],
                    "release_date": movie["release_date"],
                    "poster_path": movie["poster_path"]
                }
                for movie in data["results"]
            ]
            return jsonify(movies), 200
        else:
            logging.error(f"TMDB API response does not contain 'results' key: {data}")
            return jsonify({"error": "Failed to fetch movies by keyword"}), 500
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching movies by keyword from TMDB API: {e}")
        return jsonify({"error": "Failed to fetch movies by keyword"}), 500

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"msg": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "Username already exists"}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Email already exists"}), 400
    
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        session['user_id'] = user.id
        session['username'] = user.username
        return jsonify({"msg": "Logged in successfully"}), 200
    return jsonify({"msg": "Invalid username or password"}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return jsonify({"msg": "Logged out successfully"}), 200

@app.route('/profile', methods=['GET', 'PUT'])
@login_required
def profile():
    user = User.query.get(session['user_id'])
    if request.method == 'GET':
        return jsonify(username=user.username, email=user.email, bio=user.bio), 200
    elif request.method == 'PUT':
        data = request.json
        user.bio = data.get('bio', user.bio)
        db.session.commit()
        return jsonify({"msg": "Profile updated successfully"}), 200

@app.route('/movie/<int:tmdb_id>', methods=['GET'])
def get_movie(tmdb_id):
    movie = Movie.query.filter_by(tmdb_id=tmdb_id).first()
    if movie:
        return jsonify(id=movie.id, title=movie.title, overview=movie.overview), 200
    return jsonify({"msg": "Movie not found"}), 404

@app.route('/tv/<int:tmdb_id>', methods=['GET'])
def get_tv_show(tmdb_id):
    tv_show = TVShow.query.filter_by(tmdb_id=tmdb_id).first()
    if tv_show:
        return jsonify(id=tv_show.id, name=tv_show.name, overview=tv_show.overview), 200
    return jsonify({"msg": "TV Show not found"}), 404

@app.route('/post', methods=['POST'])
@login_required
def create_post():
    data = request.json
    new_post = Post(content=data['content'], user_id=session['user_id'], club_id=data['club_id'])
    if 'movie_id' in data:
        new_post.movie_id = data['movie_id']
    elif 'tv_show_id' in data:
        new_post.tv_show_id = data['tv_show_id']
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"msg": "Post created successfully"}), 201

@app.route('/clubs', methods=['GET'])
def get_clubs():
    clubs = Club.query.all()
    return jsonify([{"id": club.id, "name": club.name, "genre": club.genre} for club in clubs]), 200

@app.route('/club', methods=['POST'])
@login_required
def create_club():
    data = request.json
    new_club = Club(name=data['name'], description=data['description'], 
                    genre=data['genre'], created_by_id=session['user_id'])
    db.session.add(new_club)
    db.session.commit()
    return jsonify({"msg": "Club created successfully"}), 201

@app.route('/club/<int:club_id>/join', methods=['POST'])
@login_required
def join_club(club_id):
    user = User.query.get(session['user_id'])
    club = Club.query.get(club_id)
    if club not in user.clubs:
        user.clubs.append(club)
        db.session.commit()
        return jsonify({"msg": "Joined club successfully"}), 200
    return jsonify({"msg": "Already a member of this club"}), 400

@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    data = request.json
    new_comment = Comment(content=data['content'], user_id=session['user_id'], post_id=post_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"msg": "Comment added successfully"}), 201

@app.route('/post/<int:post_id>/rate', methods=['POST'])
@login_required
def rate_post(post_id):
    data = request.json
    new_rating = Rating(score=data['score'], user_id=session['user_id'], post_id=post_id)
    db.session.add(new_rating)
    db.session.commit()
    return jsonify({"msg": "Rating added successfully"}), 201

@app.route('/user/<int:user_id>/follow', methods=['POST'])
@login_required
def follow_user(user_id):
    if session['user_id'] == user_id:
        return jsonify({"msg": "You cannot follow yourself"}), 400
    follower = User.query.get(session['user_id'])
    followed = User.query.get(user_id)
    if followed is None:
        return jsonify({"msg": "User not found"}), 404
    if follower.is_following(followed):
        return jsonify({"msg": "Already following this user"}), 400
    follower.follow(followed)
    db.session.commit()
    return jsonify({"msg": "You are now following this user"}), 200

@app.route('/watched', methods=['GET', 'POST'])
@login_required
def manage_watched_movies():
    if request.method == 'GET':
        watched = WatchedMovie.query.filter_by(user_id=session['user_id']).all()
        return jsonify([{"movie_id": w.movie_id, "watched_at": w.watched_at} for w in watched]), 200
    elif request.method == 'POST':
        data = request.json
        new_watched = WatchedMovie(user_id=session['user_id'], movie_id=data['movie_id'])
        db.session.add(new_watched)
        db.session.commit()
        return jsonify({"msg": "Movie added to watched list"}), 201

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    movies = Movie.query.filter(Movie.title.ilike(f'%{query}%')).all()
    tv_shows = TVShow.query.filter(TVShow.name.ilike(f'%{query}%')).all()
    users = User.query.filter(User.username.ilike(f'%{query}%')).all()
    clubs = Club.query.filter(Club.name.ilike(f'%{query}%')).all()
    
    results = {
        "movies": [{"id": m.id, "title": m.title} for m in movies],
        "tv_shows": [{"id": t.id, "name": t.name} for t in tv_shows],
        "users": [{"id": u.id, "username": u.username} for u in users],
        "clubs": [{"id": c.id, "name": c.name} for c in clubs]
    }
    return jsonify(results), 200
