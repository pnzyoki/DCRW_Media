import React, { useEffect, useState } from 'react';
import axios from 'axios';
import dayjs from 'dayjs';
// import PhotoCarousel from './PhotoCarousel';
import CommentSection from './CommentSection';

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

  const groupedPhotos = photos.reduce((groups, photo) => {
    const date = dayjs(photo.uploaded_at).format('YYYY-MM-DD');
    if (!groups[date]) {
      groups[date] = [];
    }
    groups[date].push(photo);
    return groups;
  }, {} as Record<string, Photo[]>);

  return (
    <div>
    {Object.keys(groupedPhotos).map(date => (
      <div key={date}>
        <h2 className="text-xl font-bold">{date}</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {groupedPhotos[date].map(photo => (
            <div key={photo.id} className="border p-4">
              <img src={photo.image} alt={photo.description} className="w-full h-64 object-cover" />
              <p className="mt-2">{photo.description}</p>
              <CommentSection photoId={photo.id} />
            </div>
          ))}
        </div>
      </div>
    ))}
  </div>
  );
};

export default PhotoGrid;
