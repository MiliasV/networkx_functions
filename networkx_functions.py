#!/usr/bin/python3

import networkx as nx
import csv
import networkx as nx
import pickle
import time
import numpy as np
import matplotlib.pyplot as plt
import collections
from random import randint
from random import choice
import statistics

# create graph from the edgeList
def create_graph(edgeList, type):
    if type==0:
        G=nx.Graph()
    else:
        G = nx.DiGraph() 
    for edge in edgeList:
        G.add_edge(edge[0], edge[1])
    return G

def main():
    # My code here
    pass

if __name__ == "__main__":
    main()