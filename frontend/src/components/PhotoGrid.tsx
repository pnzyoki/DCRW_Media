import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Photo {
  id: number;
  image: string;
  uploaded_at: string;
  description: string;
}

const PhotoGrid: React.FC = () => {
  const [photos, setPhotos] = useState<Photo[]>([]);

  useEffect(() => {
    const fetchPhotos = async () => {
      try {
        const response = await axios.get('/api/photos/');
        console.log(response.data); // Log the response data
        if (Array.isArray(response.data)) {
          setPhotos(response.data);
        } else {
          console.error('Expected an array but got:', response.data);
        }
      } catch (error) {
        console.error('Error fetching photos:', error);
      }
    };

    fetchPhotos();
  }, []);

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {photos.map(photo => (
        <div key={photo.id} className="border p-4">
          <img src={photo.image} alt={photo.description} className="w-full h-64 object-cover" />
          <p className="mt-2">{photo.description}</p>
        </div>
      ))}
    </div>
  );
};

export default PhotoGrid;
