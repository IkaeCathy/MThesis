##import matplotlib
##matplotlib.use('GTKAgg')
import xml.etree.ElementTree as ET
import numpy as np
import numpy 
import cv2
from matplotlib import pyplot as plt
from matplotlib import image as image
import networkx as nx
import matplotlib.image as mpimg
from matplotlib.collections import LineCollection
import time


#used to extract cordinates and edges from a .gxl file  and draw the coordinates on a graph... 
#tree = ET.parse(gxlfile)
def coord_point(tree): 
    #extract the cordinate x, y values
    L_node_value=[]
    for node in tree.findall(".//node/attr/float"):
        L_node_value.append(node.text)
    #create a dictinary of the cordinates
    coordinate = []
    sum_x=0
    sum_y=0
    for i in range(0,len(L_node_value),2):   
        x=L_node_value[i]
        sum_x = sum_x+ float(x)
        y=L_node_value[i+1]
        sum_y = sum_y+ float(y)
        [coordinate.append([x,y])]
    return coordinate

def coord_dict(tree):
    L_id=[]
    for id in tree.findall(".//node"):
        id = id.get('id')
        L_id.append(id)
    #nodes and their coresponding id
    nodes_and_id = dict(zip(L_id, coord_point(tree)))
    return nodes_and_id
    
def node_list(tree):
    for attr in tree.findall(".//attr"):
        attr = attr.get('name')
    node_edge_List =[]
    cnt = 0
    L_cnt=[]
    #extract edges
    for edge in tree.findall(".//edge"):
        cnt = cnt +1
        L_cnt.append(str(cnt))
        start = int(edge.get('from'))
        end = int(edge.get('to'))
        node_edge=[start, end]
        [node_edge_List.append(node_edge)]
    return node_edge_List
    #Dic_edge_List = dict(zip(L_cnt,node_edge_List))
    #return Dic_edge_List

def plot_grap(points, edges):
    points= numpy.array(points)
    edges = numpy.array(edges)
    x = points[:,0].flatten()
    y = points[:,1].flatten()
    plt.plot(x[edges.T], y[edges.T], linestyle='-', color='y',
        markerfacecolor='red', marker='o', markersize=10) #ndarray.T Same as self.transpose()
   
    



    
