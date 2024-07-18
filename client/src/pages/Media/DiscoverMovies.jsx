import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './DiscoverMovies.css';

const DiscoverMovies = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchDiscoverMovies = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:10000/discover/movies');
        setMovies(response.data);
      } catch (error) {
        console.error('Error fetching discover movies:', error);
      }
    };
    fetchDiscoverMovies();
  }, []);

  return (
    <div className="discover-movies">
      <h2>Discover Movies</h2>
      {Array.isArray(movies) && movies.length > 0 ? (
        <ul className="movies-list">
          {movies.map((movie) => (
            <li key={movie.id} className="movie-item">
              <img src={`${IMAGE_URL_W300}${movie.poster_path}`} alt={movie.title} className="movie-poster" />
              <h3 className="movie-title">{movie.title}</h3>
              <p className="movie-overview">{movie.overview}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default DiscoverMovies;
