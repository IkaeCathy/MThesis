
#L_bound.py for determing the bounds

import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
import networkx 
import networkx as nx
import time
import math



def Ln_bound(alpha, tn, sourceGraph_nodes, targetGraph_nodes):

    Ln = abs((len(targetGraph_nodes) - len(sourceGraph_nodes))*(alpha*tn))
    return Ln

def Le_bound(alpha, te,source_neighbor, target_neighbor):

    Le = abs((len(target_neighbor) - len(source_neighbor))*((1-alpha)*te))
    return Le

#end
