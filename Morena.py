import cv2
import numpy as np
import pafy 
url = ['2MFL-CYiI8Y','t7cEUDuNSJE','6VChOpJt6AY']
for url in url:

	video = pafy.new(url)
	best = video.getbest(preftype="mp4")

	cap = cv2.VideoCapture() 
	cap.open(best.url)

	while True:
		ret, frame = cap.read() 
		cv2.imshow('1_0',frame)
		k = cv2.waitKey(24)&0xFF
		if k == 27:
			break
    
cap.release()
cv2.destroyAllWindows()