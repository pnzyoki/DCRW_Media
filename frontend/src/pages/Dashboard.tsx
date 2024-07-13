import React from 'react';
import PictureUpload from '../components/PictureUpload';

const Dashboard: React.FC = () => {
  return (
    <div className="p-4">
      <h2 className="text-2xl mb-4">Admin Dashboard</h2>
      <PictureUpload />
    </div>
  );
}

export default Dashboard;