from igraph import *
import numpy as np
import matplotlib.pyplot as plt

edgelist = [(0, 1), (0, 2), (0, 3),
            (1, 2), (1, 3),
            (2, 3),
            ]

g = Graph(edgelist)

trans = []
cc = []
trans.append(g.transitivity_undirected())
cc.append(g.transitivity_avglocal_undirected())
for i in np.arange(20):
    g.add_vertices([i + 4])
    g.add_edges([(i + 3, i + 4)])
    trans.append(g.transitivity_undirected())
    cc.append(g.transitivity_avglocal_undirected())

dif = [trans[i]-cc[i] for i in np.arange(len(cc))]

plt.plot(np.arange(len(cc)), cc, label='cc')
plt.plot(np.arange(len(trans)), trans, label='trans')
plt.plot(np.arange(len(trans)), dif, label='dif')
plt.legend()
plt.show()
g.vs["label"] = g.vs.indices

# print "trans: " + str(g.transitivity_undirected())
# print "cc: " + str(g.transitivity_avglocal_undirected())

layout = g.layout("kk")
plot(g, layout=layout)
