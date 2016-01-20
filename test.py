"""
create a barabasi albert network
compute its network statistics
"""
import networkx as nx
import numpy as np


WS = nx.watts_strogatz_graph(10000, 2, 0.5)
BA = nx.barabasi_albert_graph(10000, 2)
randomN = nx.watts_strogatz_graph(10000, 2, 1)
ring = nx.watts_strogatz_graph(10000, 2, 0)


print "mean BA", np.mean(BA.degree().values())
print "mean WS", np.mean(WS.degree().values())
print "mean random", np.mean(randomN.degree().values())
print "ring", np.mean(ring.degree().values())

a = 4/2

print a