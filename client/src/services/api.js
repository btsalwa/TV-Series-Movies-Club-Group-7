import axios from 'axios';

const APP_URL = 'http://127.0.0.1:10000';

export const login = async (username, password) => {
  const response = await axios.post(`${APP_URL}/login`, { username, password });
  return response.data;
};

export const register = async (username, email, password) => {
  const response = await axios.post(`${APP_URL}/register`, { username, email, password });
  return response.data;
};

export const getClubs = async () => {
  const response = await axios.get(`${APP_URL}/clubs`);
  return response.data;
};

// // // Add more API calls as needed
// // const TMDB_API_KEY = 'e407ef47003f178633c02269142f8b86';

// // const tmdbApi = axios.create({
// //   baseURL: 'https://api.themoviedb.org/3/',
// //   headers: {
// //     'Content-Type': 'application/json',
// //     'Authorization': `Bearer ${TMDB_API_KEY}`,
// //   },
// // });

// // export const getMovies = async () => {
// //   const response = await tmdbApi.get('/movie/popular', {
// //     params: {
// //       api_key: TMDB_API_KEY,
// //       language: 'en-US',
// //       page: 1,
// //     },
// //   });
// //   return response.data.results;
// // };

// // export const getTvShows = async () => {
// //   const response = await tmdbApi.get('/tv/popular', {
// //     params: {
// //       api_key: TMDB_API_KEY,
// //       language: 'en-US',
// //       page: 1,
// //     },
// //   });
// //   return response.data.results;

// // };

// // Add more API calls for other movie and TV show data