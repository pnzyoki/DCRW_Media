import React from 'react';
import PhotoGrid from '../components/PhotoGrid';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const Home: React.FC = () => {
  return (
    <>
      <Navbar />
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-4">Photo Gallery</h1>
        <PhotoGrid />
      </div>
      <Footer />
    </>
  );
};

export default Home;
