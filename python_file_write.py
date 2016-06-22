import cv2
import numpy as np

# This function accepts 2 lists, 1st-list of areas & 2nd-list of contours
def maximum_index(my_list , contours):
    # Bounding rect is drawn only if contours are detected
    if len(my_list) > 0:
        x,y,w,h = cv2.boundingRect(contours[my_list.index(max(my_list))])
        #print w , h
        if w > 135 and w < 250 and h > 130 and h < 220: # 90, 131, 80, 125
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            return 1
        elif w > 90 and w < 131 and h > 80 and h < 125: # 90, 131, 80, 125
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            return 2
        elif w > 30 and w < 90 and h > 40 and h < 80: # 10, 90, 20, 80
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

            return 3
        #print "Width= " + str(w)
        #print "Heigh= " + str(h)

        # The reason for this function is if a list is empty then max()
        # gives an error
        
    else:
        return 0
        
f = open("Records.txt", "w")

# Ranges for blue 
lower_blue = np.array([100,80,25])#69,66,15
upper_blue = np.array([160,150,85])#190,145,40

# Ranges for red 
lower_red = np.array([40,10,180])#9,0,131
upper_red = np.array([100,80,230])#50,30,220

# Ranges for yellow
lower_yellow = np.array([20,130,130])#0,118,122
upper_yellow = np.array([120,198,180])#37,146,151

# initialize counters
count_blue_type1, count_blue_type2, count_blue_type3, count_red_type1, count_red_type3, count_red_type2, count_yellow_type1, count_yellow_type2, count_yellow_type3 = 0, 0, 0, 0, 0, 0, 0, 0, 0

cap = cv2.VideoCapture(0)# 2

while True:
    _, img = cap.read()
    # The inner loop increments counters for red, blue, yellow
    
    mask_blue = cv2.inRange(img, lower_blue, upper_blue) 
    mask_red = cv2.inRange(img, lower_red, upper_red)
    mask_yellow = cv2.inRange(img, lower_yellow, upper_yellow) 

    contours_blue, heirarchy = cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    contours_red, heirarchy = cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    contours_yellow, heirarchy = cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # It draws the rectangle around blue object using the above maximum_index function
    area_list_blue = []
    for i in range(len(contours_blue)):
        area_list_blue.append(cv2.contourArea(contours_blue[i]))
    
    size_blue = maximum_index(area_list_blue, contours_blue)
    
    if size_blue:
        if size_blue == 1:
            count_blue_type1 += 1
        elif size_blue == 2:
            count_blue_type2 += 1
        elif size_blue == 3:
            count_blue_type3 += 1
    
    # It draws the rectangle around red object using the above maximum_index function
    area_list_red = []
    for i in range(len(contours_red)):
        area_list_red.append(cv2.contourArea(contours_red[i]))
    
    size_red = maximum_index(area_list_red, contours_red)
    
    if size_red:
        if size_red == 1:
            count_red_type1 += 1
        elif size_red == 2:
            count_red_type2 += 1
        elif size_red == 3:
            count_red_type3 += 1
    
    # It draws the rectangle around yellow object using the above maximum_index function    
    area_list_yellow = []
    for i in range(len(contours_yellow)):
        area_list_yellow.append(cv2.contourArea(contours_yellow[i]))

    size_yellow = maximum_index(area_list_yellow, contours_yellow)
    
    if size_yellow:
        if size_yellow == 1:
            count_yellow_type1 += 1
        elif size_yellow == 2:
            count_yellow_type2 += 1
        elif size_yellow == 3:
            count_yellow_type3 += 1
    
    ######################################################################        

    #cv2.imshow("Window", img)
    
    if cv2.waitKey(1) == 27:
        break

# counters are divided by 20 because we assume that fps of cam is 20 or 18   
print "Count blue_type1: " + str(count_blue_type1 / 12)#18
print "Count blue_type2: " + str(count_blue_type2 / 12)#18
print "Count blue_type3: " + str(count_blue_type3 / 12)#18
print "Count red_type1: " + str(count_red_type1 / 12)
print "Count red_type2: " + str(count_red_type2 / 12)
print "Count red_type3: " + str(count_red_type3 / 12)
print "Count yellow_type1: " + str(count_yellow_type1/ 12)
print "Count yellow_type2: " + str(count_yellow_type2/ 12)
print "Count yellow_type3: " + str(count_yellow_type3/ 12)

#cv2.imwrite("Temp.jpg",img)

f.write("Count Blue_type1 : " + str(count_blue_type1 / 12) + "\n")
f.write("Count Blue_type2 : " + str(count_blue_type2 / 12) + "\n")
f.write("Count Blue_type3 : " + str(count_blue_type3 / 12) + "\n")
f.write("Count Red_type1 : " + str(count_red_type1 / 12) + "\n")
f.write("Count Red_type2 : " + str(count_red_type2 / 12) + "\n")
f.write("Count Red_type3 : " + str(count_red_type3 / 12) + "\n")
f.write("Count Yellow_type1 : " + str(count_yellow_type1 / 12) + "\n")
f.write("Count Yellow_type2 : " + str(count_yellow_type2 / 12) + "\n")
f.write("Count Yellow_type3 : " + str(count_yellow_type3 / 12) + "\n")

cv2.destroyAllWindows()
cap.release()

f.close()
