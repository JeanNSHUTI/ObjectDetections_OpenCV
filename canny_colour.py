#This code is an extension of the code canny2.py
#by including features from the cannyjpg.py code.
#It allows to show the main frame, the canny edges frame
#and the frame combing the two of these frames
#Press h to subtract hue -1, 'shift' + h to add hue +1
#Press j to subtract hue -5, 'shift' + j to add hue +5
#Press w to subtract width -2, 'shift' + w to add width +2
#Last modified by Jean-Rene Nshuti

import numpy as np
import cv2
# init all available cameras
caps = [cv2.VideoCapture(0)]
i = 0

# define the HSV boundaries 
rangelower = np.array([0, 60, 40], dtype=np.uint8) #Limit the amount of grey(@param2) and luminosity (@param3) permissible 
rangeupper = np.array([255, 255, 255], dtype=np.uint8)

hue = 128
wid = 256
while(caps[-1].isOpened()): # while last VideoCapture is and existing camera
	i += 1
	caps.append(cv2.VideoCapture(i))     #Add all existing/connected cameras on current PC to list caps
caps.pop() # suppress last which is not camera

while(True):
	#Fix the maximum value 255 and minimum value at 0 for boundaries
	rangelower[0] = np.uint8(np.max(np.array([0, hue-wid/2])))
	rangeupper[0] = np.uint8(np.min(np.array([255, hue+wid/2])))
	key = 0xFF
	i = 0
	for cap in caps: # for each camera
		# Capture frame-by-frame
		ret, frame = cap.read()
		# Our operations on the frame come here
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#cv2.imshow('frame',gray)
		edges = cv2.Canny(frame,100,200)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		# find the colors within the specified boundaries and apply
		# the mask
		#The cv2.inRange  function expects three arguments: the first is the image  
		#on which we are going to perform color detection, the second is the lower  
		#limit of the color you want to detect, and the third argument is the upper  
		#limit of the color you want to detect.
		mask = cv2.inRange(hsv, rangelower, rangeupper)
		framemasked = cv2.bitwise_and(frame,frame,mask = mask)
		#print("edges= ",edges.shape)   #Shape = <480,640>
		#print("frame= ",framemasked.shape)
		
		#Convert edges (tuple) to numpy array(image frame) and
		#make its dimensions equal to framemasked for addition of two images
		array_edges = np.array([edges,edges,edges]) #Shape = <3,480,640>
		array_edges = np.transpose(array_edges, (1,2,0))
		#print("array_edges= ",array_edges.shape)  #Shape = <480,640,3>
		#print("frame= ",framemasked.shape)    #Shape = <480,640,3>
		
		#Dimensions of two image frames has to be equal in order to add images
		canny_color = cv2.add(array_edges,framemasked)  
		# Display the resulting images
		cv2.imshow('Cam' + str(i) + '_Canny',edges)
		cv2.imshow('framemasked',framemasked)
		cv2.imshow('canny_color',canny_color)

		i += 1 # next camera index for figure name
		key_ = cv2.waitKey(1) & 0xFF # waitKey necessary to display image
		if key_ != 0xFF: # if key pressed
			key = key_
	if key == ord('q'): # press 'q' to quit
		break
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
