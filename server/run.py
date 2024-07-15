from app import create_app
from app.models import fetch_and_store_tmdb_data


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='10000', debug=True)
    fetch_and_store_tmdb_data()
