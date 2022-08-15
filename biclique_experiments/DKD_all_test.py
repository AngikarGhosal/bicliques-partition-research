from IPython import embed
from utils import *
import numpy as np
import pandas as pd
import scipy as sp
import scipy.optimize as sop

all_bicliques=['1 2 4 5 <-> 10 11 13 14','2 5 <-> 10 11 13 14 12 15','5 <-> 10 11 13 14 12 15 16 17 18','4 5 <-> 10 11 13 14 16 17',
'1 2 3 4 5 6 <-> 11 14','2 3 5 6 <-> 11 14 12 15','5 6 <-> 11 14 12 15 17 18','4 5 6 <-> 11 14 17','1 2 4 5 7 8 <-> 13 14','2 5 8 <-> 13 14 15',
'5 8 <-> 13 14 15 16 17 18','4 5 7 8 <-> 13 14 16 17','1 2 3 4 5 6 7 8 9 <-> 14','2 3 5 6 8 9 <-> 14 15','5 6 8 9 <-> 14 15 17 18',
'4 5 6 7 8 9 <-> 14 17']

#Documentation
#scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='highs', callback=None, options=None, x0=None, integrality=None)
#A_ub and b_ub have <= signs
#If you have >= inequalities, multiply A_eq and b_eq by -1 to get A_ub and b_ub
#Scipy optimize is ONLY FOR MINIMIZE
#If you need to maximize a value, multiply c by -1

X=obtain_all_tuples_of_nodes(all_bicliques)
Edges=list(obtain_set_of_unique_edges(X))


BicliqueSet=list(obtain_all_bicliques(X))


M=[[0 for i in range(len(BicliqueSet))] for j in range(len(Edges))]

for i in range(len(BicliqueSet)):
    List_of_Edges=list(obtain_set_of_edges_from_biclique(*(BicliqueSet[i])))
    L0=BicliqueSet[i][0].split(" ")
    L1=BicliqueSet[i][1].split(" ")
    for edge in List_of_Edges:
        edge_position=Edges.index(edge)
        ##Sanity Check
        if edge!=Edges[edge_position]:
            print("FALSE")
        if edge[0] not in L0:
            print(edge, L0, "L0")
        if edge[1] not in L1:
            print(edge, L1, "L1")
        #Outputs Nothing
        if edge[0] in L0 and edge[1] in L1:
            M[edge_position][i]=1

Mx=np.array(M)

#scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='highs', callback=None, options=None, x0=None, integrality=None)

c=np.array([1 for i in range(Mx.shape[1])])
integrality_d=np.array([1 for i in range(Mx.shape[1])])
integrality_c=np.array([0 for i in range(Mx.shape[1])])
bounds=(0,1)
A_eq=Mx
b_eq=np.array([1 for i in range(Mx.shape[0])])

A_ub=Mx*(-1)
b_ub=b_eq*(-1)


disc_cover=sop.linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
frac_cover=sop.linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
disc_part=sop.linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
frac_part=sop.linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

print(disc_cover.fun)
print(frac_cover.fun)
print(disc_part.fun)
print(frac_part.fun)

embed()
#linprog always minimizes c dot x