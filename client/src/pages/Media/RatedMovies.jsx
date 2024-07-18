import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RatedMovies = () => {
  const [ratedMovies, setRatedMovies] = useState([]);

  useEffect(() => {
    const fetchRatedMovies = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:10000/guest-session/rated/movies');
        setRatedMovies(response.data);
      } catch (error) {
        console.error('Error fetching rated movies:', error);
      }
    };
    fetchRatedMovies();
  }, []);

  return (
    <div>
      <h2>Rated Movies</h2>
      {Array.isArray(ratedMovies) && ratedMovies.length > 0 ? (
        <ul>
          {ratedMovies.map((movie) => (
            <li key={movie.id}>
              <h3>{movie.title}</h3>
              <p>Rating: {movie.rating}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default RatedMovies;
