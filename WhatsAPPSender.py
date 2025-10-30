import pywhatkit as pwk

import datetime
import pyautogui
import keyboard as k

import time
import random

def sendInfoWA(watertype):
   
    perc=0
    
    if(watertype=="algae_water"):
        perc=random.randint(15,25)
        
    if(watertype=="industrial_polluted_water"):
        perc=random.randint(80,100)
            
    if(watertype=="muddy_water"):
        perc=random.randint(50,60)
          
    if(watertype=="shar_water"):
        perc=random.randint(15,35)
             
    percentage=str(perc)

  
    lat="19.57733"
    longi="74.44567"
    urlstr="https://www.google.com/maps/dir/"+lat+","+longi
    message="ALERT ALERT ALERT !!! \n"+ " Water pollution is detected  with type :"+ watertype+" and with level of Pollution "+percentage+" % in the following location  \n"
    message=message+urlstr+"\n ";
    message=message+". And also attached Surveilliance Image for your reference. PLEASE TAKE ACTION IMMMEDIATLY \n ";
    message=message+" Regards - \n Automatic Water Pollution  Detection System"
   
 
    reference_image_path="temp.jpg"
    mobilenumber="+919112826868"
   # WhatsAppSender.sendImage(mobilenumber, reference_image_path, message)
    # datet=str(datetime.datetime.now())
    # st=datet.split(" ")
    # kt=st[1].split(":")
    # hourstr=kt[0]
    # minstr=kt[1]
    # hr=int(hourstr)
    # min=int(minstr)
    # if(min<59):
    #     min=min+1
    # else:
    #     min=1
    #     hr=hr+1
    # print(hr)
    # print(min)
    
   
   # pwk.sendwhats_image(mobilenumber,reference_image_path,message,10,False,3)
    pwk.sendwhats_image(mobilenumber,reference_image_path,message)
    # pyautogui.click(1796,965)
    # time.sleep(2)
    # k.press_and_release('enter')
    
    
    
    
 
# # if __name__ == '__main__':
# #     sendInfoWA()
 
# sendInfoWA("muddy")   