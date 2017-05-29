import numpy as np
import cv2
import os
import glob
old_settings = np.seterr(all='ignore')

horzlino=1920
vertlino=1080


Direct="CAMR/"
rightcamcode=np.load(Direct+"coloccod.npy" )
Direct="CAML/"
leftcamcode=np.load(Direct+"coloccod.npy" )

thresholdleft=np.load("thresholdleft.npy" )
thresholdright=np.load("thresholdright.npy" )

imgmaskrightf ="CAMR/CAM001.png"
img1=cv2.imread(imgmaskrightf,cv2.IMREAD_GRAYSCALE)
ret,img1 = cv2.threshold(img1,thresholdright,255,cv2.THRESH_TOZERO)
imgmaskright=np.divide(img1,img1)

imgmaskleftf ="CAML/CAM101.png"
img1=cv2.imread(imgmaskleftf,cv2.IMREAD_GRAYSCALE)
ret,img1 = cv2.threshold(img1,thresholdleft,255,cv2.THRESH_TOZERO)
imgmaskleft=np.divide(img1,img1)

kkl=0
kkr=0
colocright=[]
colocleft=[]

leftsrt=[]
rightsrt=[]
# finding similar points in both camera bast on projected pattern
for ii in range(0, horzlino):
    for jj in range(0, vertlino):
        if (rightcamcode[jj][ii][0]!=0 and rightcamcode[jj][ii][1]!=0 and imgmaskright[jj][ii]!=0):
           colocright.append(np.uint32([rightcamcode[jj][ii][0]+rightcamcode[jj][ii][1]*1024 ,ii, jj]))
           rightsrt.append(rightcamcode[jj][ii][0]+rightcamcode[jj][ii][1]*1024)
           kkl=kkl+1
        if (leftcamcode[jj][ii][0]!=0 and leftcamcode[jj][ii][1]!=0 and imgmaskleft[jj][ii]!=0):
           colocleft.append(np.uint32([leftcamcode[jj][ii][0]+leftcamcode[jj][ii][1]*1024,ii ,jj]))
           leftsrt.append(leftcamcode[jj][ii][0]+leftcamcode[jj][ii][1]*1024)
           kkr=kkr+1

print kkr,kkl
np.savetxt("leftcod" , colocleft ,fmt='%d', delimiter=', ', newline='\n')
np.savetxt("rightcod" , colocright ,fmt='%d', delimiter=', ', newline='\n')

import operator
colocrightsrt=[]
colocleftsrt=[]
colocrightsrt=sorted(colocright, key=operator.itemgetter(0))
colocleftsrt=sorted(colocleft, key=operator.itemgetter(0))
rightsrtt=sorted(rightsrt)
leftsrtt=sorted(leftsrt)

kkr=0
np.save("colocrightsrt" , colocrightsrt)
np.save("colocleftsrt" , colocleftsrt)
newlistl=np.unique(leftsrtt)
np.savetxt("colocleftsrtuniq" , newlistl ,fmt='%d', delimiter=', ', newline='\n')
newlistr=np.unique(rightsrtt)
np.savetxt("colocrightsrtuniq" , newlistr ,fmt='%d', delimiter=', ', newline='\n')

#finding common points in both cameras
camunio=np.intersect1d(newlistl,newlistr)

kkl=0
kkr=0
kk=0
matchpixels=np.zeros((np.size(camunio),4), dtype=np.int16)
matchpixels[kk][0]=0
matchpixels[kk][1]=0
matchpixels[kk][2]=0
matchpixels[kk][3]=0
for i in camunio:
    while (newlistr[kkr] != i):
        kkr=kkr+1
        matchpixels[kk][0]=colocrightsrt[kkr][1]  # right camera x pixel coordinate
        matchpixels[kk][1]=colocrightsrt[kkr][2]  # right camera y pixel coordinate
    while (newlistl[kkl] != i):
        kkl=kkl+1
        matchpixels[kk][2]=colocleftsrt[kkl][1]   #left camera x pixel coordinate
        matchpixels[kk][3]=colocleftsrt[kkl][2]   #left camera y pixel coordinate
    kk=kk+1
    


np.savetxt("colocuniq" , matchpixels ,fmt='%d', delimiter=',', newline='\n')
print 'calcxy1xy2 Done!'
