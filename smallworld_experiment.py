import numpy as np
import matplotlib.pyplot as plt
from igraph import *

numberOfSamples = 50
probs = [1e-04, 2e-04, 3e-04, 4e-04, 5e-04,
         0.001, 0.002, 0.003, 0.004, 0.005,
         0.01, 0.02, 0.03, 0.04, 0.05,
         0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45,
         0.5, 0.6, 0.7, 0.8, 0.9, 1]
avgPL = []
trans = []

for p in probs:
    tempAPL = 0
    tempCC = 0
    for i in np.arange(1, numberOfSamples, 1):
        g = GraphBase.Watts_Strogatz(dim=1, size=1000, nei=10, p=p)
        tempAPL = tempAPL + g.average_path_length()
        tempCC = tempCC + g.transitivity_avglocal_undirected()

    tempAPL = tempAPL / numberOfSamples
    avgPL.append(tempAPL)

    tempCC = tempCC / numberOfSamples
    trans.append(tempCC)

f1 = plt.figure(1)
plt.plot(probs, avgPL, label='avgPlt')
plt.legend()

f2 = plt.figure(2)
plt.plot(probs, trans, label='CC')
plt.legend()

plt.show()
