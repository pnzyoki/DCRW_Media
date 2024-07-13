import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../axiosInstance';

const Login: React.FC =() => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('http://localhost:8000/api/token/', { username, password });
      localStorage.setItem('token', response.data.token);
      navigate('/dashboard');
    } catch (error) {
      console.error('Login failed', error);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form className="bg-white p-6 rounded shadow-md w-full max-w-sm" onSubmit={handleLogin}>
        <h2 className="text-2xl mb-4">Admin Login</h2>
        <div className="mb-4">
          <label className="block mb-1" htmlFor="username">Username</label>
          <input className="w-full p-2 border border-gray-300 rounded" type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div className="mb-4">
          <label className="block mb-1" htmlFor="password">Password</label>
          <input className="w-full p-2 border border-gray-300 rounded" type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <button className="w-full bg-blue-500 text-white p-2 rounded" type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;