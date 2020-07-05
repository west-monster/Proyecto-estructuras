import os, io
from google.cloud import vision
from google.cloud.vision import types 
import pandas as pd
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
    
    with open('IA.json', 'w') as file:
        json.dump(l, file)


if __name__ == "__main__":
    file_name = '/Users/west_mon/Desktop/pru/ja.jpg'
    identify(file_name)


    






