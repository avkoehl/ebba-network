import networkx as nx

## FUNCTIONS: parse csv line into source and targets
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

## OBJECTS: file and graph
f = open ("results_10_2017.csv", "r")
G = nx.Graph()

## MAIN: read in adjacency list and write as GEXF format

# add edges to graph
for line in f:
    source,targets = parse(line)
    for t in targets:
        exploded = t.split(' ')
        G.add_edge(source, exploded[0], weight=exploded[1])

# write in GEXF format
nx.write_gexf(G, "impressions_10_2017.gexf")



