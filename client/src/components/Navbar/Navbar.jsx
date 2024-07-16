import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Navbar.css'

const Navbar = () => {
  const history = useNavigate();


  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">Movie Club</Link>
      </div>
      <ul className="navbar-nav">
      
      </ul>
    </nav>
  );
};

export default Navbar;
