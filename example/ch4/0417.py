# 0417.py
# 영상 연산 1: 영상 덧셈
import cv2
import numpy as np

src1 = cv2.imread('./data/cat.jpg')
src2 = np.zeros(shape = (343, 515, 3), dtype = np.uint8) + 100

dst1 = src1 + src2
dst2 = cv2.add(src1, src2)
#dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows