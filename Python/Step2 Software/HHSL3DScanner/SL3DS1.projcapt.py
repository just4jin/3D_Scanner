import cv2
import sys

CV_CAP_PROP_BRIGHTNESS=10
CV_CAP_PROP_CONTRAST=11
CV_CAP_PROP_SATURATION=12
CV_CAP_PROP_EXPOSURE=15
CV_CAP_PROP_WHITE_BALANCE=17
## video capture right camera
video_capture0 = cv2.VideoCapture(0)
video_capture0.set(CV_CAP_PROP_BRIGHTNESS,30.0)
video_capture0.set(CV_CAP_PROP_CONTRAST,5.0)
video_capture0.set(CV_CAP_PROP_SATURATION,100.0)
video_capture0.set(CV_CAP_PROP_EXPOSURE,-8.0)
video_capture0.set(CV_CAP_PROP_WHITE_BALANCE,10000.0)

print video_capture0.get(4)
video_capture0.set(3,1920.0)
video_capture0.set(4,1080.0)
print video_capture0.get(4)

## video capture left camera
video_capture1 = cv2.VideoCapture(1)
print video_capture1.get(4)
video_capture1.set(3,1920.0)
video_capture1.set(4,1080.0)
print video_capture1.get(4)
print video_capture1.get(9)

video_capture1.set(CV_CAP_PROP_BRIGHTNESS,30.0)
video_capture1.set(CV_CAP_PROP_CONTRAST,5.0)
video_capture1.set(CV_CAP_PROP_SATURATION,100.0)
video_capture1.set(CV_CAP_PROP_EXPOSURE,-8.0)
video_capture1.set(CV_CAP_PROP_WHITE_BALANCE,10000.0)

## camera properties in opencv
##CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
##CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
##CV_CAP_PROP_FPS Frame rate.
##CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
##CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
##CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
##CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
##CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
##CV_CAP_PROP_HUE Hue of the image (only for cameras).
##CV_CAP_PROP_GAIN Gain of the image (only for cameras).
##CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
##CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
##CV_CAP_PROP_WHITE_BALANCE Currently unsupported
##CV_CAP_PROP_RECTIFICATION Rectificat


#show frames from cameras
ret, frame0 = video_capture0.read()
cv2.imshow("cam0", frame0)
ret, frame1 = video_capture1.read()
cv2.imshow("cam1", frame1)
cv2.waitKey(3000)

ret, frame0 = video_capture0.read()
cv2.waitKey(100)
##    cv2.imshow("cam0", frame0)
ret, frame1 = video_capture1.read()
cv2.waitKey(100)

cv2.destroyAllWindows()
horzlino=1280
vertlino=720
for ii in range(0,19):
    print ii, video_capture1.get(ii)
## open a borderless window for showing projector images as a second display    
cv2.namedWindow("Projector Window",cv2.WND_PROP_FULLSCREEN )
cv2.setWindowProperty("Projector Window", 0,1)
cv2.resizeWindow("Projector Window", 1024,768)
cv2.moveWindow("Projector Window", 1025, -2)

## folders for saving images of left and right cameras
import os
try:
    os.makedirs(textvalcap+"/"+'CAMR')
except OSError:
    pass

try:
    os.makedirs(textvalcap+"/"+'CAML')
except OSError:
    pass

imggray=np.load('proj.npy')
# Capture images from left and right cameras after showing pattern in projector
for x in range(1, 43):
    cv2.imshow("Projector Window",imggray[:,:,x-1])
    filename0 = 'CAMR/CAM0%02d.png'%(x,)
    filename1 = 'CAML/CAM1%02d.png'%(x,)
    print filename0
    ret, frame0 = video_capture0.read()
    cv2.waitKey(100)
    ret, frame1 = video_capture1.read()
    cv2.waitKey(100)
    cv2.imwrite(filename0,frame0)
    cv2.imwrite(filename1,frame1)

video_capture0.release()
video_capture1.release()
# When everything is done, release the capture
cv2.destroyAllWindows()
print 'pcapture Done!'
