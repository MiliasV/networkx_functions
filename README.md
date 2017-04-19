# networkx_functions

Custom functions to be used with the networkx module.

### create_graph(edgeList, type)
Create graph from  edge list e.g. [(1,2),(1,3),...]
If type is 0 graph is undirected. 
If type is 1 graph is directed.

### create_aggr_network(file)
Create aggregated graph from csv.
Format of file: vertex 1, vertex 2, timestamp

### create_edgelist_per_time(file)
Creaton of dictionary with the edgelist per time  {"0":[(1,2),(5,6)...], "1":[(4,7)...]...}

### plot_Dict(d, mycolor, topic, label
plot values of dictionary (xlabel = size of d) and save figures   in path/topic/label.png

### average_dict(dictionary)
average value of dictionary

### writeToCsv(csvList, topic, file)
write List to csv
