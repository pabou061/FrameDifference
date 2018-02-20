import numpy as np 
import cv2


vid = cv2.VideoCapture("video/park.avi")

if (vid.isOpened()== False): 
	print("Error opening video stream or file")

# get all properties
count = int(vid.get(7))
width= int(vid.get(3))
height=int(vid.get(4))
framerate= int(vid.get(5))

#create an empty video to save all our new frames
out = cv2.VideoWriter('result.avi',-1, framerate, (width,height),1)

#loop through all the frames
for frame_no in range(count):
    vid.set(1,frame_no)

    #read current frame 
    ret, frame_current = vid.read()
    #read next frame 
    ret1,frame_next= vid.read()

    #in case of errpr:
    if  ret == False or ret1==False:
    	break
    else:
    	# get the difference in pixels
        diff = cv2.subtract(frame_current,frame_next)
        #create the threshold
        _ ,thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        #write it in the video
        out.write(thresh)
     
#release the resources
vid.release()
out.release()
