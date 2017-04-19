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

def create_aggr_network(file):
    G=nx.Graph()    

    #create graph from csv
    with open(file, "rt") as csvfile:
        mydata = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in mydata:
            if row[0]!="" and row[1]!="" and row[2]!="":    
                vertex1 = int(row[0])
                vertex2 = int(row[1])
                G.add_edge(vertex1,vertex2)
    return G 

def create_edgelist_per_time(file): #create edgelist 
    timeD = {}  # Dictionary with the edgelist per time  {"0":[(1,2),(5,6)...], "1":[(4,7)...]...}
    with open(file, "rt") as csvfile:
        mydata = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in mydata:
            if row[0]!="" and row[1]!="" and row[2]!="":

                vertex1 = int(row[0])
                vertex2 = int(row[1])
                t = int(row[2])
            
                # Create edgelist per time - Adding one edge at a time
                if t in timeD:
                    timeD[t].append((vertex1, vertex2))
                else:
                    timeD[t]=[]
                    timeD[t].append((vertex1, vertex2))
    return timeD

def main():
    # My code here
    pass

if __name__ == "__main__":
    main()