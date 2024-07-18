import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const history = useNavigate();
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    history.push(`/search?q=${searchTerm}`);
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">Movie Club</Link>
      </div>
      <ul className="navbar-nav">
        <li className="nav-item">
          <Link to="/movies">Movies</Link>
          <ul className="dropdown-menu">
            <li><Link to="/movies/discover">Discover Movies</Link></li>
            <li><Link to="/movies/find">Find by ID</Link></li>
            <li><Link to="/movies/genres">Movie Genres</Link></li>
            <li><Link to="/movies/rated">Rated Movies</Link></li>
            <li><Link to="/movies/keywords">Keywords</Link></li>
          </ul>
        </li>
        <li className="nav-item">
          <Link to="/tv-shows">TV Shows</Link>
          <ul className="dropdown-menu">
            <li><Link to="/tv-shows/discover">Discover TV Shows</Link></li>
            <li><Link to="/tv-shows/find">Find by ID</Link></li>
            <li><Link to="/tv-shows/genres">TV Genres</Link></li>
            <li><Link to="/tv-shows/rated">Rated TV Shows</Link></li>
            <li><Link to="/tv-shows/rated-episodes">Rated TV Episodes</Link></li>
            <li><Link to="/tv-shows/keywords">Keywords</Link></li>
          </ul>
        </li>
        <li className="nav-item">
          <form onSubmit={handleSubmit}>
            <input
              type="search"
              value={searchTerm}
              onChange={handleSearch}
              placeholder="Search"
            />
            <button type="submit">Search</button>
          </form>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
