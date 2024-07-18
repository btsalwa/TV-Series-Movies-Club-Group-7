import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Keywords = () => {
  const [keyword, setKeyword] = useState('');
  const [keywordDetails, setKeywordDetails] = useState(null);
  const [keywordMovies, setKeywordMovies] = useState([]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.get(`http://127.0.0.1:10000/keywords/${keyword}`);
      setKeywordDetails(response.data);

      const moviesResponse = await axios.get(`http://127.0.0.1:10000/keywords/${keyword}/movies`);
      setKeywordMovies(moviesResponse.data);
    } catch (error) {
      console.error('Error fetching keyword details:', error);
    }
  };

  return (
    <div>
      <h2>Keywords</h2>
      <form onSubmit={handleSubmit}>
        {/* ... */}
      </form>
      {keywordDetails && (
        <div>
          <h3>{keywordDetails.name}</h3>
          <p>{keywordDetails.description}</p>
        </div>
      )}
      <h3>Movies with this Keyword</h3>
      {Array.isArray(keywordMovies) && keywordMovies.length > 0 ? (
        <ul>
          {keywordMovies.map((movie) => (
            <li key={movie.id}>
              <h4>{movie.title}</h4>
              <p>{movie.overview}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Keywords;
