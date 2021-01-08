# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:54:47 2020

@author: USER
"""

import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

# face recognition function
def objDetect() :
    obj_cascade = cv2.CascadeClassifier('cascade.xml')
    
    # Camera Setting
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened() == False:
        print ('Can\'t open the CAM')
    
    cap.set(3, 680) # set video widht
    cap.set(4, 600) # set video height
    
    print("widht: ", cap.get(3))
    print("heihgt: ", cap.get(4))
    
    count = 0
    
    while True :
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        
        if not ret :
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        objs = obj_cascade.detectMultiScale(
            gray, 
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (100, 100)
        )
        
        # draw
        for (x, y, w, h) in objs :
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        # update
        cv2.imshow('Demo01', frame)
        
        count += 1
        
        if cv2.waitKey(1) > 0 : 
            break
    
    # Destory all
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    objDetect()