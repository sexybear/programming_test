from numpy import *
import scipy
import scipy.cluster.hierarchy as sch
import matplotlib.pylab as plt

A = [6,12,18,24,30,42,48]
X = array([[6],[12],[18],[24],[30],[42],[48]])
#print type(X)
d = sch.distance.pdist(X)
Z= sch.linkage(d,method='single')
#print Z
P =sch.dendrogram(Z)
#print P
plt.savefig('plot_dendrogram.png')
T = sch.fcluster(Z, 0.5*d.max(), 'distance')
sch.leaders(Z,T)
