

#N_neighbor.py Finding the neighbors of each node in a graph

import xml.etree.ElementTree as ET
from matplotlib import pyplot as plt
import networkx as nx
import time
from plotgraph1 import *
import math


def neighborhood(G, node, n):
    path_lengths = nx.single_source_dijkstra_path_length(G, node)
    return [node for node, length in path_lengths.items()
                    if length == n]


##end

