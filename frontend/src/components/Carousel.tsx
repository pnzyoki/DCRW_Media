
interface Picture {
  id: number;
  image: string;
  upload_date: string;
  review: string;
  download_count: number;
}

const Carousel = ({ pictures }: { pictures: Picture[] }) => {
  return (
    <div className="carousel flex overflow-x-scroll space-x-4">
      {pictures.map((picture) => (
        <div key={picture.id} className="carousel-item relative">
          <img src={picture.image} alt={`Uploaded on ${picture.upload_date}`} className="w-full h-auto" />
          <button className="absolute bottom-4 right-4 bg-blue-500 text-white p-2 rounded">
            Download
          </button>
        </div>
      ))}
    </div>
  );
}

export default Carousel;