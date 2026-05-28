# 0203.py
import cv2
from matplotlib import pyplot as plt

imageFile = './data/cat.jpg'
imgRGB = cv2.imread(imageFile)
imgRGB = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2RGB)    # cv2.IMPREAD_COLOR
plt.axis('off')
#plt.imshow(imgRGB)
#plt.show()

imgRGB = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)

plt.show()