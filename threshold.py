# program that reads in a csv adjacency list and outputs 
# another adjacency list that only has the matches that are larger than threshold

def parse( line ):
    line = line.rstrip()
    elements = line.split(',')
    
    # get source
    source = elements[1]

    # get targets and weights
    targets = []
    for element in elements[2:]:
        targets.append(element)

    return (source, targets)

## configure
threshold = 7
inputfile = open ("./data/flickr/results_flickr.csv", "r")
outputfile = open ("./data/flickr/threshold_results_flickr.csv", "a")


## main
for line in inputfile:

    new_targets = []
    source, targets = parse(line)
    for t in targets:
        exploded = t.split(' ')
        distance = exploded[1]
        edge = exploded[0]
        if int(distance) > 7:
            new_targets.append(t)

    new_targets_string = ",".join(new_targets)
    name = source.split(' ')[0]

    print (name + "," + source + "," + ",".join(new_targets), file=outputfile)

            


