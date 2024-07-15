import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getMovies, getTvShows } from '/home/btsalwa/class/p4/TV-Series-Movies-Club-Group-7/client/src/services/api.js';
import './Navbar.css'

const Navbar = () => {
  const history = useNavigate();
  const [movies, setMovies] = useState([]);
  const [tvShows, setTvShows] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const movieData = await getMovies();
      const tvShowData = await getTvShows();
      setMovies(movieData);
      setTvShows(tvShowData);
    };
    fetchData();
  }, []);

  const handleLogout = () => {
    // Implement logout functionality
    localStorage.removeItem('token');
    history.push('/login');
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">Movie Club</Link>
      </div>
      <ul className="navbar-nav">
        <li className="nav-item">
          <Link to="/movies">
            Movies <span>({movies.length})</span>
          </Link>
        </li>
        <li className="nav-item">
          <Link to="/tv-shows">
            TV Shows <span>({tvShows.length})</span>
          </Link>
        </li>
        <li className="nav-item">
          <Link to="/calenda">Calenda</Link>
        </li>
        <li className="nav-item">
          <Link to="/discover">Discover</Link>
        </li>
        <li className="nav-item">
          <Link to="/club">Club</Link>
        </li>
        <li className="nav-item">
          <button className="btn btn-join" onClick={handleRegister}>
            Join
          </button>
        </li>
        <li className="nav-item">
          <button className="btn btn-logout" onClick={handleLogin}>
            Sign In
          </button>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
