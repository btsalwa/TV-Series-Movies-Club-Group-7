import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MovieGenres = () => {
  const [genres, setGenres] = useState([]);

  useEffect(() => {
    const fetchMovieGenres = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:10000/genres/movies');
        setGenres(response.data);
      } catch (error) {
        console.error('Error fetching movie genres:', error);
      }
    };
    fetchMovieGenres();
  }, []);

  return (
    <div>
      <h2>Movie Genres</h2>
      {Array.isArray(genres) && genres.length > 0 ? (
        <ul>
          {genres.map((genre) => (
            <li key={genre.id}>{genre.name}</li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default MovieGenres;
