#!/usr/bin/env python
import os, io
from google.cloud import vision
from google.cloud.vision import types 
import json

def identify(file_path):    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"token.json"

    client = vision.ImageAnnotatorClient()
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    #pylint: disable=no-member 
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    l = []
    for label in labels:
        l.append(dict(description=label.description, score = label.score))
    print(l)
    with open('IA.json', 'w') as file:
        json.dump(l, file)


if __name__ == "__main__":
    if os.path.isfile(r"C:\xampp\htdocs\e2\backend\img.jpg"):
        file_name = r"C:\xampp\htdocs\e2\backend\img.jpg"
    if os.path.isfile(r"C:\xampp\htdocs\e2\backend\img.png"):
        file_name = r"C:\xampp\htdocs\e2\backend\img.png"
    if os.path.isfile(r"C:\xampp\htdocs\e2\backend\img.jpeg"):
        file_name = r"C:\xampp\htdocs\e2\backend\img.jpeg"
    
    identify(file_name)


    






