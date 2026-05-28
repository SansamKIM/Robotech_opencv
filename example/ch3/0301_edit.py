#0301.py
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    cx, cy = w // 2, h // 2

    cv2.line(frame, (cx - 45, cy), (cx - 12, cy), (0, 255, 0), 2)
    cv2.line(frame, (cx + 12, cy), (cx + 45, cy), (0, 255, 0), 2)
    cv2.line(frame, (cx, cy - 45), (cx, cy - 12), (0, 255, 0), 2)
    cv2.line(frame, (cx, cy + 12), (cx, cy + 45), (0, 255, 0), 2)
    cv2.circle(frame, (cx, cy), 2, (0, 255, 0), -1)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
