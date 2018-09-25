#Hausdorff edit distance HEdist


import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import networkx as nx
import time
from plotgraph1 import *
#from Length_edge import *
from N_neighbor import *
from HEC2 import *
from L_bound import *
import math
import itertools



def HEdist(alpha, tn, te, sourceGraph_nodes, sourceGraph_nodesid, sourceGraph_edges, G1, targetGraph_nodes, targetGraph_nodesid, targetGraph_edges,G2):

    
    sum_delete = 0
    sum_insert = 0
    
    w2, h2 = len(sourceGraph_nodes), 1
    Matrix2 = [[0 for x in range(w2)] for y in range(h2)]
    
    w3, h3 = len(targetGraph_nodes), 1
    Matrix3 = [[0 for x in range(w3)] for y in range(h3)]
    
    
#-------create array of delete costs----------------------    
    for i in range(len(sourceGraph_nodesid)):
        delete_source_node = (alpha)*tn
        node1 = sourceGraph_nodesid[i]
        source_neighbor =   G1.neighbors(node1)#neighborhood(G1, node1, 1)
        delete_source_edge = len(source_neighbor)*((1-alpha)*te)
        Matrix2[0][i] = delete_source_node + delete_source_edge/2 #this value changes due to the number of neighbours a node has
    delete = Matrix2 #delete a node and all its edges
    

#-------create array of insert costs----------------------       
    for j in range(len(targetGraph_nodesid)):
        insert_target_node = (alpha)*tn
        node2 = targetGraph_nodesid[j]
        target_neighbor =  G2.neighbors(node2)#neighborhood(G2, node2, 1)
        insert_target_edge = len(target_neighbor)*((1-alpha)*te)
        Matrix3[0][j] =  insert_target_node + insert_target_edge/2        
    insert = Matrix3# insert a node and all its edges
    

#------------compare substituton cost to the delete cost------------------------------
#first obtain the lowest substitution cost from one node in G1 to all nodes in G2
#This value is then compared with the delete cost.
#repeat this process untill all G1 nodes are covered
    for i in range(len(sourceGraph_nodesid)):
        node1 = sourceGraph_nodesid[i]
        source_neighbor =  G1.neighbors(node1)
        List3 = []
        for j in range(len(targetGraph_nodesid)):
            node2 = targetGraph_nodesid[j]
            target_neighbor =  G2.neighbors(node2)

            Ce_all = HEC(alpha, te, source_neighbor, target_neighbor)
            
            Le = Le_bound(alpha, te, source_neighbor, target_neighbor)
            
            Ce = max(Le, Ce_all)
            
            p0 = sourceGraph_nodes[i]
            
            p1 = targetGraph_nodes[j]
            #need to separate the variables here to handle node cost and the added edge cost to determine the edit path
            #include i and j at each stage to know which is being substituted..........................................

            List3.append((alpha* (math.sqrt((float(p0[0]) - float(p1[0]))**2 + (float(p0[1]) - float(p1[1]))**2)))+(Ce/2))
           
        substitute_node = min(List3 or [0])# max(list or [0])will capture only the edge edit cost for the corresponding nodes
            
        sum_delete = sum_delete + min((substitute_node/2), delete[0][i])#subtract the edge edit cost and Ce if delete
        
#---------compare substitute cost to the insert cost-----------------------------------
#first obtain the lowest substitution cost from one node in G2 to all nodes in G1
#This value is then compared with the insert cost.
#repeat this process untill all G2 nodes are covered        
    for i in range(len(targetGraph_nodesid)):
        node2 = targetGraph_nodesid[i]
        target_neighbor =  G2.neighbors(node2)#neighborhood(G2, node2, 1)
        List4 = []
        for j in range(len(sourceGraph_nodesid)):
            node1 = sourceGraph_nodesid[j]
            source_neighbor =  G1.neighbors(node1)#neighborhood(G1, node1, 1)
            Ce_all = HEC(alpha, te, source_neighbor, target_neighbor) #i and j interchanged....i now goes with G2 and j with G1
            Le = Le_bound(alpha, te, source_neighbor, target_neighbor)
            Ce = max(Le, Ce_all)
            p1 = sourceGraph_nodes[j]
            p0 = targetGraph_nodes[i]
            List4.append((alpha* (math.sqrt((float(p0[0]) - float(p1[0]))**2 + (float(p0[1]) - float(p1[1]))**2)))+(Ce/2))

        substitute_node = min(List4 or [0])
        
        sum_insert = sum_insert + min((substitute_node/2), insert[0][i])#subtract the edge edit cost and Ce if delete
                     
    D  =  sum_delete + sum_insert
    Ln = Ln_bound(alpha, tn, sourceGraph_nodes, targetGraph_nodes)
    d =   max(Ln, D)
    return d


#end
