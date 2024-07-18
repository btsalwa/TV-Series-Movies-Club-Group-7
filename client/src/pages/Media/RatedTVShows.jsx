import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RatedTVEpisodes = () => {
  const [ratedTVEpisodes, setRatedTVEpisodes] = useState([]);

  useEffect(() => {
    const fetchRatedTVEpisodes = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:10000/guest-session/rated/tv-episodes');
        setRatedTVEpisodes(response.data);
      } catch (error) {
        console.error('Error fetching rated TV episodes:', error);
      }
    };
    fetchRatedTVEpisodes();
  }, []);

  return (
    <div>
      <h2>Rated TV Episodes</h2>
      {Array.isArray(ratedTVEpisodes) && ratedTVEpisodes.length > 0 ? (
        <ul>
          {ratedTVEpisodes.map((episode) => (
            <li key={episode.id}>
              <h3>{episode.name}</h3>
              <p>Rating: {episode.rating}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default RatedTVEpisodes;
