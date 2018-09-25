
#HEC1.py for calculating the edge edit costs

import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
import networkx as nx
import time
from plotgraph1 import *
import math

def HEC(alpha, te,  source_neighbor,  target_neighbor):


    
    sum_delete_source_edge = 0
    sum_insert_target_edge = 0    
       

    delete_source_edge = (1-alpha)*te
        
    insert_target_edge = (1-alpha)*te
                
    for i in range(len(source_neighbor)):         
                        
        substitute_edge = 0#since edges are not labeled................
        
        delete_source_edge = min(substitute_edge/2, delete_source_edge)
           
        sum_delete_source_edge = sum_delete_source_edge + delete_source_edge

    for i in range(len(target_neighbor)):          
                        
        substitute_edge = 0#since edges are not labeled...................
            
        insert_target_edge = min(substitute_edge/2, insert_target_edge)
        sum_insert_target_edge = sum_insert_target_edge + insert_target_edge
            
    Ce  =  sum_delete_source_edge + sum_insert_target_edge
    return Ce

#end

