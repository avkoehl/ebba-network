### Arthur Koehl
# PYTHON 3
# Program that updates the 
# adjacency list output of scanDB index
# inserts as the second row the cluster id
# output form: imagename, 2, imagename 100, image2 19, image3 12...
# writes output into new csv file


####################################################################
### READ IN THE TSV CLUSTER LIST
###     should have list called clusters = []
###     each index in cluster is the cluster id
###     each index points to list of filenames
####################################################################
f = open ("clusters_1-25_2018.txt", "r")
clusters = []
for line in f:
    line = line.rstrip()
    clusters.append(line)

f.close()

####################################################################
### READ IN THE RESULTS CSV AND ADD ENTRY THAT IS THE CLUSTER ID
### For each line in csv:
###     get the image name (elements[0])
###     find the index (idx) of that image name from clusters list
###     insert into list of elements in results (results[1:1] = idx)
####################################################################
f = open ("results_1-25_2018.csv", "r")
o = open ("matches_and_cluster_1-25_2018.csv", "w")
for line in f:
    idx = -1 #if unchanged, then not in a cluster
    line = line.rstrip()
    elements = line.split(",")
    name = elements[0]

    # for cluster in clusters, see if name is in that list
    for c in range(len(clusters)):
        if (name in clusters[c]):
            idx = c 
            break

    ##splice in the cluster id
    cid = str(idx)
    elements.insert(1, cid)

#    print new elements as a csv into new csv o
    result= (",").join(elements)
    print (result, file=o)
f.close()
o.close()





