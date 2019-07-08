import numpy as np
import matplotlib.pyplot as plt
import cv2
%matplotlib inline

image = cv2.imread('gaurav_rai.png')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(image)

cv2.imwrite('golu_rai.jpg',image)