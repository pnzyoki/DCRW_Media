import React from 'react';
import UploadForm from '../components/UploadForm';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const Admin: React.FC = () => {
  return (
    <>
      <Navbar />
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-4">Admin Panel</h1>
        <UploadForm />
      </div>
      <Footer />
    </>
  );
};

export default Admin;
