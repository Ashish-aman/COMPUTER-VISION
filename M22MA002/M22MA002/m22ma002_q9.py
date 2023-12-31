# -*- coding: utf-8 -*-
"""M22MA002_Q9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LUpUAjl1qHYM3bAYhyUY7y66hGixZAh1
"""

import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
from matplotlib.pyplot import plot as plt

img=cv.imread("/content/640px-thumb.jpg")
cv2_imshow(img)

"""1.Choosen image is AKSHARDHAM TEMPLE"""

img_gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# create the histogram
#take bin size equals 10 as mentioned in question
histr = cv.calcHist([img_gray],[0],None,[10],[0,256])

# configure and draw the histogram figure
plt(histr)
# plt.title("Grayscale Histogram")

equ = cv.equalizeHist(img_gray)
res = np.hstack((img_gray, equ))
cv2_imshow(res)

