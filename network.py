### Arthur Koehl 10-31-2017
# This program is meant to create a list of all the nodes
# and all of the connections (edges) in a graph
# in json form. The json will be read in by d3 for 
# visualizations
#

import json
import networkx as nx

## OBJECTS: input files and output file
f = open ("./data/flickr/results_flickr.csv", "r")
y = open ("./data/flickr/network_flickr.json", "w")
G = nx.Graph()


## FUNCTIONS: 
def parse( line ):
    line = line.rstrip()
    elements = line.split(',')
    
    # get source
    source = elements[0]

    # get targets and weights
    targets = []
    for element in elements[2:]:
        targets.append(element)

    return (source, targets)

def getcluster(source):
    c = open ("./data/flickr/clusters_flickr.txt", "r")
    idx = 0
    for line in c:
        if str(source) in line:
            return idx
        idx = idx + 1
    return -1


## MAIN 

nodes = []
links = []
for n, line in enumerate(f):
    node = {}
    link = {}

    source,targets = parse(line)
    idx= getcluster (source)
    node["name"] = source
    node["group"] = idx
    nodes.append(node.copy())
    G.add_node(source, group=idx)

    for t in targets:
        exploded = t.split(' ')
        distance = exploded[1]
        edge = exploded[0]
        link["source"] = source
        link["target"] = edge
        link["weight"] = int(distance)
        G.add_edge(source, edge, weight=distance)
        links.append(link.copy())


print ("{\"nodes\":", file=y)
print (json.dumps(nodes), file = y)
print (",", file=y)
print ("\"links\":", file=y)
print (json.dumps(links), file = y)
print ("}", file = y)
nx.write_gexf(G, "./data/flickr/network_flickr.gexf")
