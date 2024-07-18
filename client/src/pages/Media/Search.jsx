import React, { useState } from 'react';
import axios from 'axios';

const Search = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState({
    movies: [],
    tvShows: [],
    users: [],
    clubs: [],
  });

  const handleSearch = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:10000/search?q=${searchTerm}`);
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error searching:', error);
    }
  };

  return (
    <div>
      <h2>Search</h2>
      <input
        type="text"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
      <div>
        <h3>Movies</h3>
        {Array.isArray(searchResults.movies) && searchResults.movies.length > 0 ? (
          <ul>
            {searchResults.movies.map((movie) => (
              <li key={movie.id}>{movie.title}</li>
            ))}
          </ul>
        ) : (
          <p>No movies found.</p>
        )}
      </div>
      <div>
        <h3>TV Shows</h3>
        {Array.isArray(searchResults.tvShows) && searchResults.tvShows.length > 0 ? (
          <ul>
            {searchResults.tvShows.map((show) => (
              <li key={show.id}>{show.name}</li>
            ))}
          </ul>
        ) : (
          <p>No TV shows found.</p>
        )}
      </div>
      <div>
        <h3>Users</h3>
        {Array.isArray(searchResults.users) && searchResults.users.length > 0 ? (
          <ul>
            {searchResults.users.map((user) => (
              <li key={user.id}>{user.username}</li>
            ))}
          </ul>
        ) : (
          <p>No users found.</p>
        )}
      </div>
      <div>
        <h3>Clubs</h3>
        {Array.isArray(searchResults.clubs) && searchResults.clubs.length > 0 ? (
          <ul>
            {searchResults.clubs.map((club) => (
              <li key={club.id}>{club.name}</li>
            ))}
        </ul>
        ) : (
          <p>No clubs found.</p>
        )}
      </div>
    </div>
  );
};

export default Search;
