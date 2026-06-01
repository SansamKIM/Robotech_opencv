# 0402.py
# 채널 병합
import cv2
src = cv2.imread('./data/cat.jpg', cv2.IMREAD_GRAYSCALE)

b, g, r = cv2.split(src)    # 채널 분리
dst = cv2.merge([b, g, r])  # 채널 병합

print(type(dst))
print(dst.shape)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()