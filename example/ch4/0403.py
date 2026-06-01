# 0403.py
# 화소 접근1: 그레이 스케일 영상

import cv2
##import numpy as np

img = cv2.imread('./data/cat.jpg', cv2.IMREAD_GRAYSCALE)
img[100, 200] = 0
print(img[100:110, 200:210])

##for y in range(100, 400):
##    for x in range(200, 300):
##        img[y, x] = 0

img[100:400, 200:300] = 0
print(img[100:110, 200:210])    # ROI 접근

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
