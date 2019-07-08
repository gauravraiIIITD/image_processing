
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
%matplotlib inline 
 
image = cv2.imread('gaurav_rai.png') 

smaller_image = cv2.resize(image,(80,80)) 

plt.imshow(smaller_image)

cv2.imwrite('golu_rai3',smaller_image)