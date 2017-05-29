DIY 3D scanner based on structured light and stereo vision in Python language

http://www.instructables.com/member/hesamh/

Python language was used for programming for three reasons, one it is easy to learn and implement, two we can use OPENCV for image related routines and three it is portable among different operating system so you can use this program in windows, MAC and Linux. You can also configure the software to use with any kind of camera (webcams, SLRs or industrial cameras) or projector with native 1024X768 resolution. It is better to use cameras with more than two times resolution. To capture point cloud of object surface we should go trough five steps:

1. Projecting gray patterns and capturing images from two cameras "SL3DS1.projcapt.py"

2. Processing the 42 images of each camera and capture points codes " SL3DS2.procimages.py"

2. Adjusting threshold to select masking for areas to be processed "SL3DS3.adjustthresh.py"

4. Find and save similar points in each camera "SL3DS4.calcpxpy.py"

5 Calculate X,Y and Z coordinates of point cloud "SL3DS5.calcxyz.py"

The output is a PLY file with coordinate and color information of points on object surface.



grcod.npy is gray code to decimal conversion and proj.npy is image data for projection by projector.

Feel free to send me comments and messages
Hesam