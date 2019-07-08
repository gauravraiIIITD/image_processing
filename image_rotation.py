import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
%matplotlib inline 

image = cv2.imread('gaurav_rai.png') 

rows,cols = image.shape[:2] 

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
 
dst = cv2.warpAffine(image,M,(cols,rows)) 
plt.imshow(dst)
cv2.imwrite('golu_rai4',dst)
