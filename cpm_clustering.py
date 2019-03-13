from igraph import *
import numpy as np


# Clique Percolation Method
def cpm(g, k):
    def count_common_cliquenodes(cl1, cl2):
        count = 0
        for x in cl1:
            for y in cl2:
                if x == y:
                    count += 1
        return count

    cls = g.cliques(min=(k + 1))
    meta = Graph()
    meta.add_vertices(len(cls))
    meta.vs["label"] = [str(cl) for cl in cls]

    meta_edges = []
    for i in np.arange(len(cls)):
        for j in np.arange(i + 1, len(cls)):
            number_common_nodes = count_common_cliquenodes(cls[i], cls[j])
            if number_common_nodes >= k:
                meta_edges.append((i, j))

    meta.add_edges(meta_edges)
    meta_components = meta.components()
    clusters = []
    for component_index in np.arange(len(meta_components)):
        clusters.append(set())
        for meta_v in meta_components[component_index]:
            for org_v in cls[meta_v]:
                clusters[component_index].add(org_v)

    return [list(number_common_nodes) for number_common_nodes in clusters]


# Create hierarchical clustering for k = 0 to 5
def lectureexample():
    edgelist = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                (1, 2), (1, 4), (1, 5),
                (2, 3), (2, 4), (2, 5), (2, 6),
                (3, 4), (3, 5),
                (4, 5), (4, 6),
                (5, 9), (5, 10), (5, 11), (5, 12),
                (6, 7), (6, 8),
                (7, 8), (7, 10), (7, 11),
                (9, 10), (9, 11), (9, 12),
                (10, 11), (10, 12),
                (11, 12)

                ]
    g = Graph(edgelist)
    g.vs["label"] = g.vs.indices

    hierarcical_clustering = []
    for k in np.arange(6):
        print "k: " + str(k)

        # Do Clustering
        clustering = cpm(g, k)

        hierarcical_clustering.append(clustering)
        if len(clustering) > 0:
            for c in np.arange(len(clustering)):
                print "Cluster" + str(c) + ":" + str(clustering[c])
        else:
            print "no clustering possible"

        print "\n"

    # try to encode it clusters by color
    # Problem: overlapping clusters and nodes with single colordefinition
    #
    # colors = ["red", "blue", "green"]
    # g.vs["color"] = [colors[cluster] for cluster in g.vs["cluster"]]

    layout = g.layout("kk")
    plot(g, layout=layout, bbox=(300, 300))
