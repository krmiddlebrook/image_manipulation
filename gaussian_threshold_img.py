import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

image   = cv2.imread(os.getcwd()+'/images/'+input("Enter path to file: "), 0)    # read in image - convert to grayscale
# plt.show()

image   = cv2.bilateralFilter(image, 9, 75, 75)   # bilaterally filters the image to reduce noise, blur, and maintain edges

gauss_thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)     # finds threshold of img using gaussian nearest window technique

titles   = [str(image), 'Gaussian Thresholding']
images  = [image, gauss_thresh]


for i in range(2):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

