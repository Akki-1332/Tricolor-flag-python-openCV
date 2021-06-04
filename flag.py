import cv2
import numpy as np
#Saffron Color
saffron = cv2.imread("saffron.jpg")
saffron = saffron[0:135 , :]
cv2.imwrite("saffron_color.jpg"  , saffron )

#White Color
white = np.zeros([135, 600, 3])
white[:, :] =  [255, 255, 255]
cv2.imwrite("white_color.jpg" , white)

#Green Color
green = np.zeros([135, 600, 3])
green[:, :] =  [0, 255, 0]
cv2.imwrite("green_color.jpg" , green)

#Combining Images
s = cv2.imread("saffron_color.jpg")
w  = cv2.imread("chakr.jpg")
g = cv2.imread("green_color.jpg")
tricolor = np.vstack( (s, w, g) )

#Showing INDIAN Flag
cv2.imshow("hi", tricolor)
cv2.waitKey()
cv2.destroyWindow()

