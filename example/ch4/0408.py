# 0408.py
# 마우스로 다중 ROI 영역 지정: cv2.selctROIs()
import cv2

src = cv2.imread('./data/cat.jpg', cv2.IMREAD_GRAYSCALE)
rects = cv2.selectROIs('src', src, False, True)
print('rects =', rects)

for r in rects:
    cv2.rectangle(src, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), 255)

# 지정했던 영역 출력
##  img = src[r[1]:r[1] + r[3], r[0]:r[0] + r[2]]
##  cv2.imshow('Img', img)
##  cv2.waitKey()

'''
지정 했던 영역 새 창으로 출력
for i, r in enumerate(rects):
    cv2.rectangle(src, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), 255)
    img = src[r[1]:r[1] + r[3], r[0]:r[0] + r[2]]
    cv2.imshow(f'ROI_{i}', img)
'''

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()