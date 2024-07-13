import React, { useEffect, useState } from 'react';
import { getPictures } from '../api/api';
import Carousel from '../components/Carousel';

const Landing: React.FC = () => {
  const [pictures, setPictures] = useState([]);

  useEffect(() => {
    const fetchPictures = async () => {
      try {
        const response = await getPictures();
        setPictures(response.data);
      } catch (error) {
        console.error('Failed to fetch pictures', error);
      }
    };

    fetchPictures();
  }, []);

  return (
    <div>
      <Carousel pictures={pictures} />
    </div>
  );
}

export default Landing;