import cv2
import time
import numpy as np
import serial

ser = serial.Serial(16,timeout=1) ##opens COM port 17
cap = cv2.VideoCapture(0)

lower_red = np.array([110,120,40])#9,0,131
upper_red = np.array([150,180,75])#50,30,220
lower_blue = np.array([100,80,25])#69,66,15
upper_blue = np.array([160,150,85])#190,145,40
lower_yellow = np.array([20,130,130])#0,118,122
upper_yellow = np.array([120,198,180])#37,146,151

def detect_red(img,flag1):
    mask_red = cv2.inRange(img, lower_red, upper_red)
    cv2.imshow("newW",mask_red)
    cv2.imwrite("1.jpg",img)
    contours_red, heirarchy = cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours_red)):
        if cv2.contourArea(contours_red[i]) > 0 and flag1 == 0:
            ser.write('r')
            break
  
def detect_blue(img,flag1):
    mask_blue = cv2.inRange(img, lower_blue, upper_blue)
    contours_blue, heirarchy = cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours_blue)):
        if cv2.contourArea(contours_blue[i]) > 0 and flag1 == 0:
            ser.write('b')
            break
        
def detect_yellow(img,flag1):
    mask_yellow = cv2.inRange(img, lower_yellow, upper_yellow)
    contours_yellow, heirarchy = cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours_yellow)):
        if cv2.contourArea(contours_yellow[i]) > 0 and flag1 == 0:
            ser.write('g')
            break

initial_time = time.time() 
while True:
    flag = 0
    start_time = time.time()
    count_blue_type1, count_blue_type2, count_blue_type3, count_red_type1, count_red_type3, count_red_type2, count_yellow_type1, count_yellow_type2, count_yellow_type3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    while True:
        _, img = cap.read()

        print img[200,200]
        red = detect_red(img,flag)
#        blue = detect_blue(img,flag)
#       yellow = detect_yellow(img,flag)
        flag = 1

        cv2.imshow("Window", img)
        
        if cv2.waitKey(1) == 27:
            break
        if time.time() - start_time >= 5:
            break
        #print "Loop 2"
        print time.time() - start_time
    #print "Loop 1"
    print time.time() - initial_time
    if time.time() - initial_time >= 35:
        break

cv2.destroyAllWindows()
cap.release()
