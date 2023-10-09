import ctypes
import cv2
import pyscreenshot
import numpy as np

def getRoi():
    # get the screen size
    user32 = ctypes.windll.user32
    # get the screencapture
    bbox=(0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
    screen = np.array(pyscreenshot.grab(bbox))
    # have user select the minimap
    roi = cv2.selectROI(screen)
    cv2.destroyAllWindows()
    return roi

def getImg(roi):
    screen = np.array(ImageGrab.grab(bbox=(roi[0], roi[1], roi[0] + roi[2], roi[1] + roi[3])))
    img = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    return img

def findPointsFromCircles(roi):
    #find the circles in the image
    circles = None
    while circles is None:
        img = getImg(roi)
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=20,minRadius=1,maxRadius=10)
    # set target to the midpoint ( my best algorithm for now )
    return np.uint16(np.around(circles))[0,:]
    