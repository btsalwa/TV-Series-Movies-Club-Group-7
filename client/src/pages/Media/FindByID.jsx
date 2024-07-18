import React, { useState } from 'react';
import axios from 'axios';

const FindByID = () => {
  const [itemId, setItemId] = useState('');
  const [itemData, setItemData] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.get(`http://127.0.0.1:10000/find/${itemId}`);
      setItemData(response.data);
    } catch (error) {
      console.error('Error finding item by ID:', error);
    }
  };

  return (
    <div>
      <h2>Find by ID</h2>
      <form onSubmit={handleSubmit}>
        {/* ... */}
      </form>
      {itemData && (
        <div>
          <h3>{itemData.title}</h3>
          <p>{itemData.overview}</p>
          <p>Release Date: {itemData.release_date}</p>
          <img src={`https://image.tmdb.org/t/p/w500${itemData.poster_path}`} alt={itemData.title} />
        </div>
      )}
    </div>
  );
};

export default FindByID;
