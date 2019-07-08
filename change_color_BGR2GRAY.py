
import matplotlib.pyplot as plt 
import cv2 
%matplotlib inline 
image = cv2.imread('gaurav_rai.png') 

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

plt.imshow(gray_image) 

cv2.imwrite('golu_rai1.jpg',gray_image)
