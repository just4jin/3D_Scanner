# OpenCV
### How to use Homebrew to install OpenCV2 for Python on Mac OS

Requirements:
1. Xcode installed
2. Homebrew installed
3. Python 2 installed
4. Logged in as adminitrator account

Terminal Command Lines:
1. ```brew tap homebrew/science```
2. ```brew install opencv```
3. ```sudo su```
4. ```echo "/usr/local/lib/python2.7/site-packages/" > /Library/Python/2.7/site-packages/opencv.pth```

Try-Out:
```python```
```import cv``` (or import cv2)
```cv.__version__```

