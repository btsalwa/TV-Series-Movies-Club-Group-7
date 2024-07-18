import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RatedTVShows = () => {
  const [ratedTVShows, setRatedTVShows] = useState([]);

  useEffect(() => {
    const fetchRatedTVShows = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:10000/guest-session/rated/tv');
        setRatedTVShows(response.data);
      } catch (error) {
        console.error('Error fetching rated TV shows:', error);
      }
    };
    fetchRatedTVShows();
  }, []);

  return (
    <div>
      <h2>Rated TV Shows</h2>
      {Array.isArray(ratedTVShows) && ratedTVShows.length > 0 ? (
        <ul>
          {ratedTVShows.map((show) => (
            <li key={show.id}>
              <h3>{show.name}</h3>
              <p>Rating: {show.rating}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default RatedTVShows;
