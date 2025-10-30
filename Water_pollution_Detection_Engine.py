import cv2
import matplotlib.pyplot as plt
import numpy as np
import cv2
from ultralytics import YOLO
import random
#import EMAILSender


def startDetection():
    
    
    model_pothole = YOLO("model/water_pollution_best.pt","v8") 
   
   
    
    # frame=cv2.imread("img1.jpg")
    
    # detect_params=model.predict(frame, conf=0.4, save=False)
    cap = cv2.VideoCapture(2)
    
    
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    count=0 
    
    while True:
        ret, frame = cap.read()
    
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
    
       #print(model.predict("your_image.jpg", confidence=40, overlap=30).json())
        detect_params_pothole = model_pothole.predict(source=[frame], conf=0.1, save=False)
       # detect_params_roadhumps = model_roadhump.predict(source=[frame], conf=0.1, save=False)
        
    
        class_list=["algae_water","clear_water","industrial_water","muddy_water","no_sample"]
        for box in detect_params_pothole[0].boxes:
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]
        
            x1 = int(bb[0])
            x2 = int(bb[2])
            y1 = int(bb[1])
            y2 = int(bb[3])
           
            text=class_list[int(clsID)]
            value=round(conf, 3)
            #print("value ",value)
            if(value>0.1):
                text = text + str(round(conf, 3)) + "%"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, text, (x1, y1), font, 1, (255, 0, 0), 2)
                count=count+1
            
            # else:
            #     text = " Pothole" + str(round(conf, 3)) + "%"
            #     cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 3)
            #     font = cv2.FONT_HERSHEY_COMPLEX
            #     cv2.putText(frame, text, (x1, y1), font, 1, (255, 255, 255), 2)
        
        
    
        
        # for box in detect_params_roadhumps[0].boxes:
        #     clsID = box.cls.numpy()[0]
        #     conf = box.conf.numpy()[0]
        #     bb = box.xyxy.numpy()[0]
        
        #     x1 = int(bb[0])
        #     x2 = int(bb[2])
        #     y1 = int(bb[1])
        #     y2 = int(bb[3])
           
        #   #  text=class_list[int(clsID)]
        #     value=round(conf, 3)
        #     #print("value ",value)
        #     if(value>0.65):
        #         text = " Road Humps" + str(round(conf, 3)) + "%"
        #         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
        #         font = cv2.FONT_HERSHEY_COMPLEX
        #         cv2.putText(frame, text, (x1, y1), font, 1, (0, 0, 255), 2)
        #         count=count+1
            
        #     # else:
        #     #     text = "  Road Humps" + str(round(conf, 3)) + "%"
        #     #     cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 3)
        #     #     font = cv2.FONT_HERSHEY_COMPLEX
        #     #     cv2.putText(frame, text, (x1, y1), font, 1, (255, 255, 255), 2)
        
        
        
        
        
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow('Pothole Detection System', frame)
            
    
            
    
    # Release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()
startDetection()
#input_video_path="input videos/pothole1.mp4"     
#startDetection(input_video_path)                        


        # reciever_email="sukeshinichemate9791@gmail.com"
        # subject="Potholes Alert"
        # body="Dear sir/madam\n There are to many patholes identified in the uploaded video for the concern, please take the action immediately.\n Thank You,\nAutomatic Pothiles Detection System"
        # EMAILSender.sendEmail(reciever_email,subject,body)
    
    
    