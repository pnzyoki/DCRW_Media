import React, { useState } from 'react';

const Dashboard = () => {
  const [images, setImages] = useState<FileList | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setImages(e.target.files);
  }

  const handleUpload = () => {
    // Implement upload logic
  }

  return (
    <div className="p-4">
      <h2 className="text-2xl mb-4">Admin Dashboard</h2>
      <div className="mb-4">
        <label className="block mb-1" htmlFor="images">Upload Pictures</label>
        <input className="w-full p-2 border border-gray-300 rounded" type="file" id="images" multiple onChange={handleFileChange} />
      </div>
      <button className="bg-blue-500 text-white p-2 rounded" onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default Dashboard;