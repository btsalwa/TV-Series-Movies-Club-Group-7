import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'default_url')
    ENVIRONMENT = os.getenv('APP_ENV', 'development')

    TMDB_BASE_URL = "https://api.themoviedb.org/3"
    TMDB_API_KEY = "e407ef47003f178633c02269142f8b86"