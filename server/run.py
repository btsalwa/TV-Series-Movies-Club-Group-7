from app import create_app
from app.models import fetch_and_store_tmdb_data


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    fetch_and_store_tmdb_data()
