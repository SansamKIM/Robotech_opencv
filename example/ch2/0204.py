# 0204.py
import cv2
from matplotlib import pyplot as plt

imageFile = './data/cat.jpg'
imGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
plt.axis('off')

plt.imshow(imGray, cmap = "gray", interpolation = 'bicubic')

plt.show()