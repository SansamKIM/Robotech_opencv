# 0404.py
# 화소 접근 2: 컬러 영상(RGB)
import cv2
##import numpy as np

img = cv2.imread('./data/cat.jpg')      # cv2.IMREAD_COLOR
img[100, 200] = [255, 0, 0]             # 컬러(RGB) 변경
print(img[100, 200:210])                # ROI 접근 
##for y in range(100, 400):
##    for x in range(200, 300):
##      img[y, x] = [255, 0, 0]

img[25:40, 25:40] = [0, 255, 0]     # ROI 접근

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()