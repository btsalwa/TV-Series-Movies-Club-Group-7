import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TVGenres = () => {
  const [genres, setGenres] = useState([]);

  useEffect(() => {
    const fetchTVGenres = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:10000/genres/tv');
        setGenres(response.data);
      } catch (error) {
        console.error('Error fetching TV genres:', error);
      }
    };
    fetchTVGenres();
  }, []);

  return (
    <div>
      <h2>TV Genres</h2>
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

export default TVGenres;
