import numpy as np
import cv2
# init all available cameras
caps = [cv2.VideoCapture(0)]
i = 0
while(caps[-1].isOpened()): # while last VideoCapture is and existing camera
	i += 1
	caps.append(cv2.VideoCapture(i))
caps.pop() # suppress last which is not camera

while(True):
	key = 0xFF
	i = 0
	for cap in caps: # for each camera
		# Capture frame-by-frame
		ret, frame = cap.read()
		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# Display the resulting frame
		#cv2.imshow('frame',gray)
		cv2.imshow('Cam' + str(i) + '_color',frame)
		edges = cv2.Canny(frame,100,200)
		cv2.imshow('Cam' + str(i) + '_Canny',edges)
		i += 1 # next camera index for figure name
		key_ = cv2.waitKey(1) & 0xFF # waitKey necessary to display image
		if key_ != 0xFF: # if key pressed
			key = key_
	if key == ord('q'): # press 'q' to quit
		break
	elif key == ord('p'): # press 'p' to print camera parameters
		list_prop = ( # id of main parameters
			'CAP_PROP_POS_MSEC',       # 0) Current position of the video file in milliseconds.
			'CAP_PROP_POS_FRAMES',     # 1) 0-based index of the frame to be decoded/captured next.
			'CAP_PROP_POS_AVI_RATIO',  # 3) Relative position of the video file
			'CAP_PROP_FRAME_WIDTH',    # 4) Width of the frames in the video stream.CAP_PROP_FRAME_HEIGHT
			'CAP_PROP_FRAME_HEIGHT',   # 5) Height of the frames in the video stream.
			'CAP_PROP_FPS',            # 6) Frame rate.
			'CAP_PROP_FOURCC',         # 7) 4-character code of codec.
			'CAP_PROP_FRAME_COUNT',    # 8) Number of frames in the video file.
			'CAP_PROP_FORMAT',         # 9) Format of the Mat objects returned by retrieve() .
			'CAP_PROP_MODE',           #10) Backend-specific value indicating the current capture mode.
			'CAP_PROP_BRIGHTNESS',     #11) Brightness of the image (only for cameras).
			'CAP_PROP_CONTRAST',       #12) Contrast of the image (only for cameras).
			'CAP_PROP_SATURATION',     #13) Saturation of the image (only for cameras).
			'CAP_PROP_HUE',            #14) Hue of the image (only for cameras).
			'CAP_PROP_GAIN',           #15) Gain of the image (only for cameras).
			'CAP_PROP_EXPOSURE',       #16) Exposure (only for cameras).
			'CAP_PROP_CONVERT_RGB',    #17) Boolean flags indicating whether images should be converted to RGB.
			# print(cap.get(cv2.CAP_PROP_WHITE_BALANCE))) #18) CAP_PROP_WHITE_BALANCE Currently unsupported
			'CAP_PROP_RECTIFICATION')  #19) Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
		if len(caps)==1:
			print('---------- Parameters of camera ----------')
		else:
			print('---------- Parameters of cameras ----------')
		for prop in list_prop:
			if len(caps)==1:
				eval( 'print("' + prop + ' : %d" % (caps[0].get(cv2.' + prop + ')))' ) # e.g., print("CAP_PROP_GAIN : %d" % (caps[0].get(cv2.CAP_PROP_GAIN)))
			elif len(caps)>1:
				instr = 'print("' + prop + ' :   '
				for i in range(len(caps)): # for each camera
					instr += '[Cam' + str(i) + ']: %d  '
				camsparam = ()
				for cap in caps: # for each camera
					camsparam = camsparam + (cap.get(eval('cv2.' + prop)), ) # append property value as tuple
				instr += '" % camsparam)'
				eval( instr ) # e.g., print("CAP_PROP_GAIN :   [Cam0]: %d  [Cam1]: %d  " % camsparam)
			else:
				print('No parameter to print because no existing camera')

# When everything done, release the capture
for cap in caps :
	cap.release()
cv2.destroyAllWindows()
