import React, { useEffect, useState } from 'react';
import { getClubs } from '../services/api';
// import ClubCard from '../components/ClubCard';

function Home() {
  const [clubs, setClubs] = useState([]);

  useEffect(() => {
    async function fetchClubs() {
      const clubsData = await getClubs();
      setClubs(clubsData);
    }
    fetchClubs();
  }, []);

  return (
    <div>
      <h1>Welcome to Movie Club</h1>
      <h2>Popular Clubs</h2>
      <div className="club-list">
        {clubs.map(club => (
          <ClubCard key={club.id} club={club} />
        ))}
      </div>
    </div>
  );
}

export default Home;
