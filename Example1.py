import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/model1.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

potato_plant = cv2.imread('C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/Dataset1/Test/Potato___Early_blight/7227b3db-c212-4370-8b42-443eea1577aa___RS_Early.B 7306.JPG')
test_image = cv2.resize(potato_plant, (128,128)) # load image 
  
test_image = img_to_array(test_image)/255 # convert image to np array and normalize
test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
result = model.predict(test_image) # predict diseased palnt or not
  
pred = np.argmax(result, axis=1)
print(pred)
if pred==0:
    print( "Potato___Early_blight")
       
elif pred==1:
    print("Potato___healthy")
        
elif pred==2:
    print("Potato___Late_blight")
        

