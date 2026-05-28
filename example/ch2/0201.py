# 0201.py
import cv2
import numpy as np

imageFile = './data/cat.jpg'
img = cv2.imread(imageFile)     # cv2.IMREAD_COLOR
img2 = cv2.imread(imageFile, 0)  # cv2.IMREAD_GRAYSCALE

## encode_img =np.fromfile(imageFile, np.uint8)
## img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)

cv2.imshow('Cat Color', img)
cv2.imshow('Cat grayscale', img2)

cv2.waitKey()
cv2.destroyAllWindows()
