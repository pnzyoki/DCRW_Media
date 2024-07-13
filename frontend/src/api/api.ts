import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export const getPictures = () => api.get('pictures/');
export const uploadPictures = (data: FormData) => api.post('pictures/', data, {
  headers: {
    'Content-Type': 'multipart/form-data'
  }
});