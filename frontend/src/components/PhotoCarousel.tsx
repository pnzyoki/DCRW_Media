import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';

interface Photo {
  id: number;
  image: string;
  description: string;
}

interface Props {
  photos: Photo[];
}

const PhotoCarousel: React.FC<Props> = ({ photos }) => {
  return (
    <Carousel>
      {photos.map(photo => (
        <div key={photo.id}>
          <img src={photo.image} alt={photo.description} />
          <p className="legend">{photo.description}</p>
        </div>
      ))}
    </Carousel>
  );
};

export default PhotoCarousel;
