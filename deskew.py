import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image

#used to determine skew angle and deskew image based on the detected skew angle

def compute_skew_angle(image):
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    height, width = image.shape
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    v = np.median(blurred)
    sigma = 0.33
    #---- apply optimal Canny edge detection using the computed median----
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))
    edges = cv2.Canny(blurred, lower_thresh, upper_thresh, 3, 5)
    #determine hough lines
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=width-2000, maxLineGap=20)    
    for x in range(0, len(lines)):
        for x1,y1,x2,y2 in lines[x]:
            cv2.line(image,(x1,y1),(x2,y2),(0, 0, 255), 2, cv2.LINE_AA)        
    angle = 0.0
    number_of_lines = lines.shape[0]
    #determine skew angle
    for x1, y1, x2, y2 in lines[0]:
        if x1 != x2:
            angle += np.arctan(y2 - y1 / x2 - x1)
    return angle / number_of_lines

def deskew(image, angle):
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    angle = np.math.degrees(angle)
    non_zero_pixels = cv2.findNonZero(image)
    #centering the image points
    center, wh, theta = cv2.minAreaRect(non_zero_pixels)
    #obtain Rotation matrix using the centered point and angle
    Rotation_mat = cv2.getRotationMatrix2D(center, angle, 1)
    rows, cols = image.shape
    #rotate the image using the rotation matrix
    rotated = cv2.warpAffine(image, Rotation_mat, (cols, rows), flags=cv2.INTER_CUBIC)
    return cv2.getRectSubPix(rotated, (cols, rows), center)

