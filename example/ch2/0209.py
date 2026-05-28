# 0209.py
'''
 pip install yt-dlp
'''
import cv2
import yt_dlp

url = 'https://www.youtube.com/watch?v=DIlw6_Ui884'

ydl_opts = {
        'format': 'best[ext=mp4]/best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print('title = ', info.get('title'))
        print('duration = ', info.get('duration'))
        print('resolution = ', f"{info.get('width')}x{info.get('height')}")
        stream_url = info['url']
        w = info.get('width', '?')
        h = info.get('height', '?')
        print(f'resolution = {w}x{h}')

cap=cv2.VideoCapture(stream_url)

while(True):
        retval, frame = cap.read()
        if not retval:
                break
        cv2.imshow('frame',frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,100,200)
        cv2.imshow('edges',edges)

        key = cv2.waitKey(25)
        if key == 27: # Esc
                break
cv2.destroyAllWindows()
