import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import Header from './components/Header';
// import Footer from './components/Footer';
import Home from './pages/Home.jsx';
import Navbar from './components/Navbar/Navbar.jsx';
// import Login from './pages/Login';
// import Register from './pages/Register';
// import Profile from './pages/Profile';
// import MovieDetails from './pages/MovieDetails';
// import ClubDetails from './pages/ClubDetails';
// import CreatePost from './pages/CreatePost';
// import CreateClub from './pages/CreateClub';

function App() {
  return (
    
    <Router>
      <Navbar />
        
      {/* <Header /> */}
      <Routes>
        <Route exact path="/" component={Home} />
        {/* <Route path="/login" component={Login} />
        <Route path="/register" component={Register} />
        <Route path="/profile" component={Profile} />
        <Route path="/movie/:id" component={MovieDetails} />
        <Route path="/club/:id" component={ClubDetails} />
        <Route path="/create-post" component={CreatePost} />
        <Route path="/create-club" component={CreateClub} /> */}
      </Routes>
      {/* <Footer /> */}
    </Router>
  );
}

export default App;