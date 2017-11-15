#Written by Professor F.Geuning (ECAM)for Image treatment class

import cv2, numpy as np
rangelower = np.array([0, 100, 40], dtype=np.uint8)
rangeupper = np.array([255, 255, 255], dtype=np.uint8)
hue = 128
wid = 256

filename = 'eurobot2018_playingarea.jpg'
frame = cv2.imread(filename)
while(True):
	rangelower[0] = np.uint8(np.max(np.array([0, hue-wid/2])))
	rangeupper[0] = np.uint8(np.min(np.array([255, hue+wid/2])))
	key = 0xFF
	cv2.imshow(filename,frame)
	# Canny
	edges = cv2.Canny(frame,100,200)
	# Color detection, ref https://henrydangprg.com/2016/06/26/color-detection-in-python-with-opencv/
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, rangelower, rangeupper)
	framemasked = cv2.bitwise_and(frame,frame,mask = mask)
	cv2.imshow('framemasked',framemasked)
	cv2.imshow('Canny',edges)
	zoom = 0.5
	cv2.imshow(filename + ' resized', cv2.resize(frame,None,fx=zoom, fy=zoom, interpolation = cv2.INTER_CUBIC))
	cv2.imshow('Canny resized', cv2.resize(edges,None,fx=zoom, fy=zoom, interpolation = cv2.INTER_CUBIC))
	key_ = cv2.waitKey(100) & 0xFF # waitKey necessary to display image
	print(key_)
	if key_ != 0xFF: # if key pressed
		key = key_
		if key == ord('q'): # press 'q' to quit
			break
		else : 
			if key == ord('h'): # hue  -1 'h'
				hue -= 1
			if key == ord('H'): # hue  +1 'H'
				hue += 1
			if key == ord('j'): # hue  -5 'j'
				hue -= 5
			if key == ord('J'): # hue  +5 'J'
				hue += 5
			if key == ord('w'): # wid  -2 'w'
				wid -= 2
			if key == ord('W'): # wid  +2 'W'
				wid += 2
			print('hue: %d   wid: %d' % (hue,  wid))

cv2.destroyAllWindows()
