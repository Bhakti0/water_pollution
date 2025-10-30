import numpy as np
import argparse
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from keras.models import load_model



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
def initTesting(shotframepath):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(96,96,3)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
        
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
        
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(9, activation='softmax'))
    model.load_weights('model/model_CNN.h5')
   
    
   
   
    
    
        # prevents openCL usage and unnecessary logging messages
    #cv2.ocl.setUseOpenCL(False)
    
   

   
   # shot_dict={0:"accident",1:"non accident"}
    img = cv2.imread(shotframepath)
    dim = (96, 96)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
   
    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(img, (96, 96)), -1), 0)
    prediction = model.predict(cropped_img)
 
    maxindex = int(np.argmax(prediction))
    print("Matched index is ",maxindex)
   # shot_name=shot_dict[maxindex]

   # return shot_name
    
    
  
    
if __name__ == '__main__':
    initTesting("testing/i.jpg")        