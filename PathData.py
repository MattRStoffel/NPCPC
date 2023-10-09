import numpy as np
from DataCapture import findPointsFromCircles

def bestNavAlgorithm(pointsSortedByRange):
    #find the closest and farthest dots
    closestDot = pointsSortedByRange[0]
    if len(pointsSortedByRange) > 1:
        farthestDot = pointsSortedByRange[1]
    else:
        farthestDot = pointsSortedByRange[-1]
    return int((closestDot[0] + farthestDot[0])/2), int((closestDot[1] + farthestDot[1])/2)
    
def findTarget(roi): 
    points = findPointsFromCircles(roi)
    pointsSortedByRange = points[np.argsort(points, axis=0)[:,0]]
    target = bestNavAlgorithm(pointsSortedByRange)
    return target

def findAngleToTarget(roi):
    target = findTarget(roi)
    return np.atan2(target[1] - roi[3]/2, target[0] - roi[2]/2) + np.pi/2# main
