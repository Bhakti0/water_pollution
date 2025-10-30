import cv2
import os
import numpy

datasetpath="Water_Dataset"


if not os.path.exists(datasetpath):
    os.makedirs(datasetpath)   

    
      
cap=cv2.VideoCapture(2)
imgeno=0

while cap.isOpened():
    _,capimg=cap.read()
  
      
   
    cv2.imshow('Anti-robbing Dataset Creator Image( Press esc to quit)',capimg)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
    # SPACE pressed
        filename=str(imgeno)   
        newfilepath=datasetpath+"//"+filename+".jpg" # anti robbing Dataset//1.jpg
     
        cv2.imwrite(newfilepath,capimg)
        imgeno=imgeno+1
        print("Image path is ",newfilepath)
  
                
          


cap.release()
cv2.destroyAllWindows()