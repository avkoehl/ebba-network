### Arthur Koehl 10-31-2017
# This program is meant to create a list of all the nodes
# and all of the connections (edges) in a graph
# in json form. The json will be read in by d3 for 
# visualizations
#

import json

## OBJECTS: input files and output file
f = open ("./data/results_1-25-2018.csv", "r")
y = open ("network_1-25-2018.json", "w")


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
    c = open ("./data/clusters_1-25-2018.txt", "r")
    idx = 0
    for line in c:
        if str(source) in line:
            print ("here")
            return idx
        idx = idx + 1
    return -1


## MAIN 

nodes = []
links = []
for line in f:
    node = {}
    link = {}

    source,targets = parse(line)
    print (source)
    idx= getcluster (source)
    node["name"] = source
    node["group"] = idx
    nodes.append(node.copy())

    for t in targets:
        exploded = t.split(' ')
        distance = exploded[1]
        edge = exploded[0]
        link["source"] = source
        link["target"] = edge
        link["weight"] = int(distance)
        links.append(link.copy())


print ("{\"nodes\":", file=y)
print (json.dumps(nodes), file = y)
print (",", file=y)
print ("\"links\":", file=y)
print (json.dumps(links), file = y)
print ("}", file = y)


