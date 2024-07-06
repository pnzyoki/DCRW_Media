import torch
from facenet_pytorch import InceptionResnetV1, MTCNN
from PIL import Image

# Initialize MTCNN and InceptionResnetV1
mtcnn = MTCNN()
resnet = InceptionResnetV1(pretrained='vggface2').eval()

def recognize_faces(photo_path):
    img = Image.open(photo_path)
    img_cropped = mtcnn(img)
    if img_cropped is not None:
        img_embedding = resnet(img_cropped.unsqueeze(0))
        return img_embedding
    return None
