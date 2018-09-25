
#Knn

import math
import operator
from HEdist13 import *
import time
import glob
from plotgraph1 import *
from deskewgraph import * 
from deskew import *
from directory import *
import numpy as np
import re
start_time = time.time()
k=1
neighbors = []
alpha = 0.5
j=0
te=5 
tn=5
j=6420
#used for classification of centered graph with 64 pations used for the matching... also tested on the one which is not centered and results were very similar..
#Taking a look at only 16 partitions.....12.12.2017............
x = list_files('C:/DATA/NIST2-small')
W = [w for w in x if w.endswith('_Harris.gxl')]
w, h = len(W), len(W);
Matrix_T_V = [[0 for x in range(w)] for y in range(h)]
Wi= [wi for wi in x if not wi.endswith('.gxl')]
file = open("Matrix_T_V" + str(j) + ".txt", "w")#The matrix files for the distances, j was was an identifier for the files being used

for tt in range(95,len(W)):
    #print(tt)
    img = Wi[tt]
    print(img)
    image = mpimg.imread(img)    
    angle = compute_skew_angle(img)    
    tree1 = ET.parse(W[tt])#('r0437_02_03_SCP.gxl')
    centered_graph1 = center_graph(tree1,angle)#.... changed to test uncerntered graphs with same number of partions
    #centered_graph1 = deskew_graph(tree1, angle)
    quadrants1 = split_into_quadrants(centered_graph1)
    condensedquadrants1 = [quadrants1[a] for a in range(4)]
    quadrants11= [split_into_quadrants(Q) for Q in condensedquadrants1]#creates a list of a list
    quadrants11 = [item for sublist in quadrants11 for item in sublist]#flatten the list
    quadrants12= [split_into_quadrants(Q1) for Q1 in quadrants11]
    quadrants12 = [item for sublist in quadrants12 for item in sublist]
    
    Distance=[]
    for ff in range(len(W)):        
        if W[ff] != W[tt]:
                start_time = time.time()
                Dist = 0
                img = Wi[ff]
                image = mpimg.imread(img)
                angle = compute_skew_angle(img)
                tree2 = ET.parse(W[ff])
                centered_graph2 = center_graph(tree2,angle)#.... changed for testing other an uncentered graph
                #centered_graph2 = deskew_graph(tree2, angle)
                quadrants2 = split_into_quadrants(centered_graph2)
                condensedquadrants2 = [quadrants2[a] for a in range(4)]                
                quadrants21= [split_into_quadrants(Q) for Q in condensedquadrants2]
                quadrants21 = [item for sublist in quadrants21 for item in sublist]
                quadrants22= [split_into_quadrants(Q1) for Q1 in quadrants21]
                quadrants22 = [item for sublist in quadrants22 for item in sublist]             
        
                for a in range(64):                    
                        #it takes an average of 5 seconds to get distance between a partition
                        sourceGraph_nodes= quadrants12[a]#changing to 16 partition... average time btn partitions is 40seconds.........
                        #.... the distance is smaller with smaller number of partition as compared to more number of partiotions......
                        #the first quadrant of the centered graph
                        #sourceGraph_nodes are nodes in the individual quadrants....
                        nodes1= centered_graph1                                               
                        sourceGraph_nodesid = [nodes1.index(x) for x in sourceGraph_nodes]#****values belonging to sourcenodes but their index in the original set
                        #print("sourceGraph_nodesid",sourceGraph_nodesid[0])#this should give whole numbers such as 1,1,3,....
                        sourceGraph_edges = [nodelist for nodelist in node_list(tree1) if set(nodelist).issubset(sourceGraph_nodesid)]
                        
                        G1 = nx.Graph()
                        nodekeys1 = coord_dict(tree1).keys()
                        G1.add_nodes_from(nodekeys1)
                        G1.add_edges_from(node_list(tree1))
                        targetGraph_nodes= quadrants22[a]
                        nodes2= centered_graph2
                        targetGraph_nodesid = [nodes2.index(x) for x in targetGraph_nodes]#values belonging to sourcenodes but their index in the original set
                        #print(sourceGraph_nodesid[0])
                        targetGraph_edges = [nodelist for nodelist in node_list(tree2) if set(nodelist).issubset(targetGraph_nodesid)]
                        G2 = nx.Graph()                
                        nodekeys2 = coord_dict(tree2).keys()
                        G2.add_nodes_from(nodekeys2)
                        G2.add_edges_from(node_list(tree2))

                        dist = HEdist(alpha, tn,te, sourceGraph_nodes, sourceGraph_nodesid, sourceGraph_edges,G1, targetGraph_nodes, targetGraph_nodesid, targetGraph_edges,G2)
                        #print("--- %s seconds ---" % (time.time() - start_time))
                        Dist+=dist
                print(W[tt],W[ff], "Distance =", float("{0:.4f}".format(Dist)))
                Matrix_T_V[tt][ff] = Dist
                B=np.array(Matrix_T_V)
                file.write("\n".join(map(str, (Matrix_T_V))))#write distance matrix to a file, at the end or at intermediate points
                #print("--- %s seconds ---" % (time.time() - start_time))
                Distance.append(Dist)
    n = [x for x in W if x != W[tt]]
    #for each querry graph file show its NN distance and matched file
    print(W[tt],n[Distance.index(min(Distance))], "min_Distance =", float("{0:.4f}".format(min(Distance))))
            
file.close() 
