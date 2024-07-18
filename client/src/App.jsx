import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import Header from './components/Header';
// import Footer from './components/Footer';
import Home from './pages/Home/Home.jsx';
import Navbar from './components/Navbar/Navbar.jsx';
import Login from './pages/Auth/Login/Login.jsx';
import Register from './pages/Auth/Register/Register.jsx';
import DiscoverMovies from './pages/Media/DiscoverMovies.jsx';
import DiscoverTVShows from './pages/Media/DiscoverTVShows.jsx';
import FindByID from './pages/Media/FindByID.jsx';
import MovieGenres from './pages/Media/MovieGenres.jsx';
import TVGenres from './pages/Media/TVGenres.jsx';
import RatedMovies from './pages/Media/RatedMovies.jsx';
import RatedTVShows from './pages/Media/RatedTVShows.jsx';
import RatedTVEpisodes from './pages/Media/RatedTVEpisodes.jsx';
import Keywords from './pages/Media/Keywords.jsx';
import Search from './pages/Media/Search.jsx';
import Profile from './pages/Profile.jsx';
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
        <Route exact path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/movies/discover" element={<DiscoverMovies />} />
        <Route path="/tv-shows/discover" element={<DiscoverTVShows />} />
        <Route path="/movies/find" element={<FindByID />} />
        <Route path="/tv-shows/find" element={<FindByID />} />
        <Route path="/movies/genres" element={<MovieGenres />} />
        <Route path="/tv-shows/genres" element={<TVGenres />} />
        <Route path="/movies/rated" element={<RatedMovies />} />
        <Route path="/tv-shows/rated" element={<RatedTVShows />} />
        <Route path="/tv-shows/rated-episodes" element={<RatedTVEpisodes />} />
        <Route path="/movies/keywords" element={<Keywords />} />
        <Route path="/tv-shows/keywords" element={<Keywords />} />
        <Route path="/search" element={<Search />} />
        <Route path="/profile" component={Profile} />
        {/* <Route path="/movie/:id" component={MovieDetails} /> */}
        {/* <Route path="/club/:id" component={ClubDetails} /> */}
        {/* <Route path="/create-post" component={CreatePost} /> */}
        {/* <Route path="/create-club" component={CreateClub} /> */}
      </Routes>
      {/* <Footer /> */}
    </Router>
  );
}

export default App;