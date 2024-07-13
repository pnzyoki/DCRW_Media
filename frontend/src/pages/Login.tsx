import React from 'react';

const Login = () => {
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form className="bg-white p-6 rounded shadow-md w-full max-w-sm">
        <h2 className="text-2xl mb-4">Admin Login</h2>
        <div className="mb-4">
          <label className="block mb-1" htmlFor="username">Username</label>
          <input className="w-full p-2 border border-gray-300 rounded" type="text" id="username" />
        </div>
        <div className="mb-4">
          <label className="block mb-1" htmlFor="password">Password</label>
          <input className="w-full p-2 border border-gray-300 rounded" type="password" id="password" />
        </div>
        <button className="w-full bg-blue-500 text-white p-2 rounded" type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;