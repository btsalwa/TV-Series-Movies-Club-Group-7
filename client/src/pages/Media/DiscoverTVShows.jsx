import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DiscoverTVShows = () => {
  const [tvShows, setTvShows] = useState([]);

  useEffect(() => {
    const fetchDiscoverTVShows = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:10000/discover/tv');
        setTvShows(response.data);
      } catch (error) {
        console.error('Error fetching discover TV shows:', error);
      }
    };
    fetchDiscoverTVShows();
  }, []);

  return (
    <div>
      <h2>Discover TV Shows</h2>
      {Array.isArray(tvShows) && tvShows.length > 0 ? (
        <ul>
          {tvShows.map((show) => (
            <li key={show.id}>
              <h3>{show.name}</h3>
              <p>{show.overview}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default DiscoverTVShows;
