grayimg=np.zeros((vertlino, horzlino), dtype=np.int16)
rightcamcode=np.zeros((vertlino, horzlino,2), dtype=np.int16)
##=======================================================
#Horizontal gray code
for ii in range(3,22,2):
    xx=ii-3
    xx=xx//2
    filename1 =  img_names[ii]
    filename2 =  img_names[ii-1]
    ff=imgdesig(filename1,filename2)
    print 'processing %s...' % filename1, (2**xx)
    grayimg=grayimg+(2**xx)*ff

imgbin3=np.zeros((vertlino, horzlino,3), dtype=np.uint8)
for ii in range(0, horzlino):
    for jj in range(0, vertlino):
        rightcamcode[jj][ii][0]=grayimg[jj][ii]
        imgbin3[jj][ii][1]= grayimg[jj][ii]%256
        imgbin3[jj][ii][2]= 40*grayimg[jj][ii]//256
        imgbin3[jj][ii][0]= 4
img1=(grayimg%255)
cv2.imshow("PWindow2",imgbin3)
cv2.waitKey(100)

##=======================================================
#Vertical gray code

img1=cv2.imread(img_names[0],cv2.IMREAD_GRAYSCALE)
grayimg=(img1*0)+1023
grayimg=grayimg*0
for ii in range(23,42,2):
    xx=ii-22
    xx=xx//2
    filename1 =  img_names[ii]
    filename2 =  img_names[ii-1]
    ff=imgdesig(filename1,filename2)
    print 'processing %s...' % filename1, (2**xx)
    grayimg=grayimg+(2**xx)*ff

for ii in range(0, horzlino):
    for jj in range(0, vertlino):
        rightcamcode[jj][ii][1]=grayimg[jj][ii]
        imgbin3[jj][ii][0]= (imgbin3[jj][ii][0]+grayimg[jj][ii]%256)%256
        imgbin3[jj][ii][2]= 40*(imgbin3[jj][ii][2]+grayimg[jj][ii]%256)//80
        imgbin3[jj][ii][1]= 4
img1=(grayimg%255)
cv2.imshow("PWindow2",imgbin3)
cv2.waitKey(2000)


