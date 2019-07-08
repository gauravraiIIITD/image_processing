
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
%matplotlib inline

image = cv2.imread('gaurav_rai.jpg') 

edges = cv2.Canny(image,200,200) 

plt.imshow(edges)