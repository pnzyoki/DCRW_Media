import React, { useState } from 'react';
import axios from 'axios';

const UploadForm: React.FC = () => {
  const [images, setImages] = useState<FileList | null>(null);
  const [descriptions, setDescriptions] = useState<string[]>([]);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setImages(e.target.files);
    }
  };

  const handleDescriptionChange = (index: number, value: string) => {
    const newDescriptions = [...descriptions];
    newDescriptions[index] = value;
    setDescriptions(newDescriptions);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new FormData();
    if (images) {
      Array.from(images).forEach((image, index) => {
        formData.append('images', image);
        formData.append('descriptions', descriptions[index] || '');
      });
      try {
        const response = await axios.post('/api/photos/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('Upload successful:', response.data);
      } catch (error) {
        console.error('Error uploading photos:', error);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" multiple onChange={handleFileChange} />
      {images &&
        Array.from(images).map((_, index) => (
          <input
            key={index}
            type="text"
            placeholder={`Description for image ${index + 1}`}
            onChange={(e) => handleDescriptionChange(index, e.target.value)}
          />
        ))}
      <button type="submit">Upload Photos</button>
    </form>
  );
};

export default UploadForm;
