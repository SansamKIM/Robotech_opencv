# 0409.py
# 영상 복사 1
import cv2
src = cv2.imread('./data/cat.jpg')

#dst = src          # 얕은 복사: src와 dst는 같은 메모리를 참조
dst = src.copy()    # 깊은 복사: src와 dst는 다른 메모리를 참조
dst[100:400, 200:300] = 0

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
