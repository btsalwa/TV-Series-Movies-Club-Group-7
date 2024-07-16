import React from 'react';
import { useNavigate } from 'react-router-dom'
import './Home.css';

function Home() {
  const navigate = useNavigate()
  return (
    <div className="home-container">
      <h1>Welcome to the Movies/Series Club App</h1>
      <p>Discover, discuss, and connect with fellow movie and TV show enthusiasts.</p>
      <div className='links-container'>
                <p>Not yet in a club</p>
                <button
                    type='button'
                    onClick={() => navigate('/register')}
                >
                    Join
                </button>
                <p>Already a club member?</p>
                <button
                    type='button'
                    onClick={() => navigate('/login')}
                >
                    Sign In
                </button>
            </div>
    </div>
  );
};

export default Home;