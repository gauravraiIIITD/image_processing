
import matplotlib.pyplot as plt 
import cv2 
%matplotlib inline 
image = cv2.imread('gaurav_rai.png') 

HSV_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

plt.imshow(HSV_image) 

cv2.imwrite('golu_rai2.jpg',HSV_image)
