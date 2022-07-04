# http://2884-18-231-84-218.ngrok.io
# https://2884-18-231-84-218.ngrok.io
import cv2
import matplotlib.pyplot as plt
import numpy as np
# imagens = plt.imread('D:\\Albert Einstein\\MARIA II\\Tuberculose\\Diversos\\teste.PNG')
imagens = plt.imread('D:\\Albert Einstein\\montgomery-dataset\\images\\images\\MCUCXR_0399_1.png')

# imagens = cv2.cvtColor(imagens, cv2.COLOR_BGR2GRAY)
dim = (299, 299)
imagens = cv2.resize(imagens, dim, interpolation = cv2.INTER_AREA)
imagens = np.stack([imagens, imagens, imagens], axis = 2)
imagens = imagens.reshape(1,299,299,3)
# imagens = imagens.reshape(1,299,299,3)

import json
data = json.dumps({"signature_name": "serving_default", "instances": imagens.tolist()})

import requests
import json
headers = {"content-type": "application/json"}
json_response = requests.post('http://2884-18-231-84-218.ngrok.io/v1/models/C19:predict', data=data, headers=headers)
scores = json.loads(json_response.text)['predictions']

boxes = scores[0].get("filtered_detections")[0]
score = scores[0].get("filtered_detections_1")[0]
labels = scores[0].get("filtered_detections_2")[0]

print(str(boxes) + " " + str(score) + " " + str(labels))

