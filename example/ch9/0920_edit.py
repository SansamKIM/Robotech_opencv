import cv2
import numpy as np

cap = cv2.VideoCapture(0)
images = []
prev_gray = None
MIN_TRANSLATION = 40

orb = cv2.ORB_create(500)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

while True:
    retval, frame = cap.read()
    if not retval:
        break
    img = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if prev_gray is None:
        images.append(img)
        prev_gray = gray
    else:
        kp1, des1 = orb.detectAndCompute(prev_gray, None)
        kp2, des2 = orb.detectAndCompute(gray, None)
        if des1 is not None and des2 is not None:
            matches = bf.match(des1, des2)
            matches = sorted(matches, key=lambda x: x.distance)[:50]
            if len(matches) >= 20:
                pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
                pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])
                translation = np.mean(np.linalg.norm(pts2 - pts1, axis=1))
                if translation > MIN_TRANSLATION:
                    images.append(img)
                    prev_gray = gray
                    print(f"[{len(images)}장 캡처]")

    cv2.putText(img, f"Images: {len(images)}  [S]stitch [ESC]quit",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
    cv2.imshow('Capture', img)

    key = cv2.waitKey(25)
    if key == 27:  # Esc
        break
    elif key == ord('s') and len(images) >= 2:
        print("스티칭 중...")
        stitcher = cv2.Stitcher.create()
        status, dst = stitcher.stitch(images)
        if status == cv2.STITCHER_OK:
            cv2.imwrite('./data/video_stitch_out.jpg', dst)
            cv2.imshow('Panorama Result', dst)
            cv2.waitKey()
        else:
            print(f"스티칭 실패 (status={status})")

cap.release()
cv2.destroyAllWindows()