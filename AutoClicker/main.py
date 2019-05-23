from PIL import ImageGrab as ig
import numpy as np
import cv2
from pynput.mouse import Button, Controller


mouse = Controller()
screen_coords1 = [200, 90, 210, 700]
screen_coords2 = [300, 90, 310, 700]
screen_coords3 = [500, 90, 510, 700]
screen_coords4 = [620, 90, 630, 700]
# screen_img1.save("./screenshot.png", "png")

pxls = []
for i in range(4):
    screen_img = None
    if(i==0):
        screen_img = ig.grab(bbox=screen_coords1)
    elif (i == 1):
        screen_img = ig.grab(bbox=screen_coords2)
    elif (i == 2):
        screen_img = ig.grab(bbox=screen_coords3)
    elif (i == 3):
        screen_img = ig.grab(bbox=screen_coords4)

    pxl_array = np.array(screen_img)
    pxl_array = cv2.cvtColor(pxl_array, cv2.COLOR_BGR2GRAY)
    pxl_array = pxl_array.tolist()
    for k in range(len(pxl_array)):
        if i == 0:
            pxls = pxl_array
            break
        else:
            pxls[k].extend(pxl_array[k])
pxls = np.array(pxls)

###
#for i in range(100):
##    for x in range(len(pxl_array)):
 #       for y in range(len(pxl_array[x])):
 #           if pxl_array[x][y] > 50 and pxl_array[x][y] < 100:
 #               print(mouse.position)
###



