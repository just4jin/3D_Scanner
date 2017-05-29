import numpy as np
import cv2
horzlino=1920
vertlino=1080
import os
import glob
img_names = glob.glob("CAML/*.png")
img1=cv2.imread(img_names[0],cv2.IMREAD_GRAYSCALE)
ii=50
# adjusting the threshold for processing area and eliminating shadows
# use left and right arrow key to adjust and press 'q' when finished

while True:
    ret,img1th = cv2.threshold(img1,ii,255,cv2.THRESH_TOZERO)
    cv2.putText(img1th,"Threshold is "+str(ii), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    cv2.imshow("PWindow2",img1th)
    k = cv2.waitKey(0)  
    if k == 113:
        break
    elif k == 2555904:
        ii=ii+1
    elif k == 2424832:
        ii=ii-1

cv2.destroyAllWindows()

np.save(captdirect+"/"+"thresholdleft" , ii)
    
img_names = glob.glob("CAMR/*.png")
img1=cv2.imread(img_names[0],cv2.IMREAD_GRAYSCALE)
ii=50
while True:
    ret,img1th = cv2.threshold(img1,ii,255,cv2.THRESH_TOZERO)
    cv2.putText(img1th,"Threshold is "+str(ii), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    cv2.imshow("PWindow2",img1th)
    k = cv2.waitKey(0)  
    if k == 113:
        break
    elif k == 2555904:
        ii=ii+1
    elif k == 2424832:
        ii=ii-1
        

cv2.destroyAllWindows()
np.save("thresholdright" , ii)
print 'Threshold Done!'
