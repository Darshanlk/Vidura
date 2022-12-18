
from deepface import DeepFace
import cv2
import os
file_set = set()
img1=cv2.imread('image1.jpg')
print(img1)
img2=cv2.imread('elon.webp')
print(img2)

result = DeepFace.verify(img1,img2)
print("Is same face: ",result["verified"])


