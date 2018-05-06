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
f = open ("./data/flickr/results_flickr.csv", "r") #make these command line arguments
y = open ("./data/flickr/edges_flickr.txt", "w")

## MAIN: read in adjacency list and output abc format for mcl 
for line in f:
    source,targets = parse(line)
    for t in targets:
        exploded = t.split(' ')
        distance = exploded[1]
        edge = exploded[0]
        print (source, edge, distance, file=y)



