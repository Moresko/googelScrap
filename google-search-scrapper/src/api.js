import axios from 'axios';

const api = axios.create({
  URL: "http://localhost:8000"
});

export default api;