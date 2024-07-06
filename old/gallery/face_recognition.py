import face_recognition
from .models import Photo, Face

def process_faces(photo):
    image = face_recognition.load_image_file(photo.image.path)
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    for face_encoding in face_encodings:
        similar_faces = Face.objects.filter(photo__face_encoding__isnull=False)
        for similar_face in similar_faces:
            if face_recognition.compare_faces([similar_face.face_encoding], face_encoding)[0]:
                photo.faces.add(similar_face)
                break
        else:
            new_face = Face.objects.create()
            new_face.face_encoding = face_encoding
            new_face.save()
            photo.faces.add(new_face)