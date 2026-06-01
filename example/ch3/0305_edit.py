# 0305_edit.py
import cv2
import numpy as np

img = np.zeros(shape=(512, 512, 3), dtype=np.uint8) + 255

shapes = [
    # square - blue - closed
    (np.array([[50, 50], [150, 50], [150, 150], [50, 150]]), (255, 0, 0), True),
    # trapezoid - green - closed
    (np.array([[250, 60], [380, 60], [420, 150], [220, 150]]), (0, 180, 0), True),
    # star - red - closed
    (np.array([
        [250, 210], [270, 260], [325, 260], [280, 290], [300, 345],
        [250, 310], [200, 345], [220, 290], [175, 260], [230, 260],
    ]), (0, 0, 255), True),
    # zigzag - orange - open
    (np.array([[50, 400], [120, 350], [190, 400], [260, 350], [330, 400]]), (0, 130, 255), False),
]

for points, color, is_closed in shapes:
    cv2.polylines(img, [points], isClosed=is_closed, color=color, thickness=2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
