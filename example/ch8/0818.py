# 0818.py
# cv2.integral() 적분 영상 2
import cv2
import numpy as np

#1
gray = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

#2
gray_sum = cv2.integral(gray)
dst = cv2.normalize(gray_sum, None, 0, 255,
                    cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()
