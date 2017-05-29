import numpy as np
import cv2
import os
import glob

def imgdesig(img1,img2): #define a function for getting dark and light pattern
   old_settings = np.seterr(all='ignore')
   img1=cv2.imread(img1,cv2.IMREAD_GRAYSCALE)
   ret,img1 = cv2.threshold(img1,10,255,cv2.THRESH_TOZERO)
   img2=cv2.imread(img2,cv2.IMREAD_GRAYSCALE)
   ret,img2 = cv2.threshold(img2,10,255,cv2.THRESH_TOZERO)
   img12=(((img1//2)+(img2//2)))
   img123=(np.divide(img1,img12))
   img123=(np.divide(img123,img123))
   return img123

horzlino=1280
vertlino=720
Direct="CAMR/"
img_names = glob.glob(Direct+"*.png")
#call for processing the right camera images
execfile("camlcoloc.py")
np.save(Direct+"coloccod" , rightcamcode)
cv2.waitKey(200)
Direct="CAML/"
img_names = glob.glob(Direct+"*.png")
#call for processing the left camera images
execfile("camlcoloc.py")
np.save(Direct+"coloccod" , rightcamcode)

cv2.destroyAllWindows()
print 'Images processing Done!'
