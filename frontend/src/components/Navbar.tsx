import React from 'react';
import { Link } from 'react-router-dom';

const Navbar: React.FC = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-white text-lg font-bold">
          Church Photos
        </Link>
        <div className="space-x-4">
          <Link to="/" className="text-white">Home</Link>
          <Link to="/admin" className="text-white">Admin</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
