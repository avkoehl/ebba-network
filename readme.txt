A series of programs useful for visualizing the network created by Archv.

[1] edges.py 
	takes as input the adjeceny list of matches
	outputs a text file where each line is a different edge
	then run mcl edges.txt --abc -o clusters.txt

[2] full_list.py
	takes as input the adjecency list and the clusters.txt file
	creates a new adjacency list that has a column with cluster id

[3] network.py
	takes as input the full adjacency list from 2
	creates in json format the graph file

[4] meta.py
	takes the full list from 2
	creates a graph file of the meta network
	the meta network is such that each cluster becomes a node
	the edges are the edges that exist between members of cluster 1 with cluster 2
	the edge weight is the number of those edges

