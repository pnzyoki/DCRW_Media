import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="bg-gray-800 text-white p-4 flex justify-between items-center">
      <h1 className="text-3xl">Church Pictures</h1>
      <nav>
        <Link to="/" className="mr-4">Home</Link>
        <Link to="/login">Admin Login</Link>
      </nav>
    </header>
  );
}

export default Header;