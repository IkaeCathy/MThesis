import xml.etree.ElementTree as ET
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import networkx as nx
import matplotlib.image as mpimg
from deskew import deskew
from deskew import compute_skew_angle
import math
from plotgraph1 import *


#used to determine new cordinates after rotation through an angle 
def deskew_graph(tree, angle):
    node_value =coord_point(tree)
    sum_x=0
    sum_y=0
    for i in range(0,len(node_value)):   
        x=node_value[i][0]
        sum_x = sum_x+ float(x)
        y=node_value[i][1]
        sum_y = sum_y+ float(y)
    center= (sum_x/(len(node_value)), sum_y/(len(node_value)))
    origin = center
    angle = -angle
    ox, oy = origin
    r_coordinates = []
    for point in range(len(node_value)):
        px, py = node_value[point]
        rx = ox + (math.cos(angle)  * (float(px) - ox) - math.sin(angle) * (float(py) - oy))
        ry = oy + (math.sin(angle) * (float(px) - ox) + math.cos(angle) * (float(py) - oy))
        [r_coordinates.append([str(rx), str(ry)])]
    return r_coordinates
    
def center_graph(tree, angle):
    node_value1 = deskew_graph(tree, angle)
    sum_x=0
    sum_y=0
    for i in range(0,len(node_value1)):   
        x=node_value1[i][0]
        sum_x = sum_x+ float(x)
        y=node_value1[i][1]
        sum_y = sum_y+ float(y)
    center= (sum_x/(len(node_value1)), sum_y/(len(node_value1)))
    origin = center
    ox, oy = origin
    c_coordinates = []
    for point in range(len(node_value1)):
        px, py = node_value1[point]
        cx =  float(px) - ox
        cy =  float(py) - oy
        [c_coordinates.append([str(cx), str(cy)])]
    return c_coordinates
    

def split_into_quadrants(points):
    data_q1=[]
    data_q2=[]
    data_q3=[]
    data_q4=[]
    xmin, ymin = min([float(points[p][0]) for p in range(len(points))]),min([float(points[p][1]) for p in range(len(points))])
    xmax, ymax = max([float(points[p][0]) for p in range(len(points))]),max([float(points[p][1]) for p in range(len(points))])
    mids = 0.5 * (float(xmin) + float(xmax)), 0.5 * (float(ymin) + float(ymax))
    xmid, ymid = mids

    for L in points:
        x, y = L      # split the data into four quadrants
        if (float(x) < mids[0])  & (float(y) < mids[1]):
            data_q1.append(L)
        elif  (float(x) < mids[0])  & (float(y) > mids[1]): #(float(y) >= mids[1])..keeps the nodes to only one region
           data_q2.append(L)     
        elif (float(x) > mids[0]) & (float(y) < mids[1]): #(float(x) >= mids[0])
            data_q3.append(L)   
        else: 
           data_q4.append(L) 
    return data_q1, data_q2, data_q3,data_q4
                
    
