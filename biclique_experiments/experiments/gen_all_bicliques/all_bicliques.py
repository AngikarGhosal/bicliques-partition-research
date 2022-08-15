from IPython import embed
from utils import *
import numpy as np
import argparse
from pathlib import Path
import os
Path("../../datafiles/AllBicliques").mkdir(parents=True, exist_ok=True)
Path("../../datafiles/Edges").mkdir(parents=True, exist_ok=True)
parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='../../datafiles/Bicliques/3DKDBicliques.txt', help='bicliques file path')

args = parser.parse_args()
file_path=args.file

with open(file_path, 'r') as filename:
    all_bicliques = filename.readlines()
    all_bicliques = [line.rstrip() for line in all_bicliques]
filename.close()
matrixtype=file_path[26:-13]

X=obtain_all_tuples_of_nodes(all_bicliques)
Edges=list(obtain_set_of_unique_edges(X))


BicliqueSet=list(obtain_all_bicliques(X))

with open("../../datafiles/AllBicliques/"+matrixtype+"allbicliques.txt", "w") as g:
    for biclique in BicliqueSet:
        x=biclique[0]+' <-> '+biclique[1]
        g.write(f"{x}\n")

with open("../../datafiles/Edges/"+matrixtype+"edges.txt", "w") as h:
    for edge in Edges:
        x=edge[0]+' <-> '+edge[1]
        h.write(f"{x}\n")

'''
M=[[0 for i in range(len(BicliqueSet))] for j in range(len(Edges))]

for i in range(len(BicliqueSet)):
    List_of_Edges=list(obtain_set_of_edges_from_biclique(*(BicliqueSet[i])))
    L0=BicliqueSet[i][0].split(" ")
    L1=BicliqueSet[i][1].split(" ")
    for edge in List_of_Edges:
        edge_position=Edges.index(edge)
        if edge[0] in L0 and edge[1] in L1:
            M[edge_position][i]=1

Mx=np.array(M)
print(Mx.shape)
print(len(Edges))
ConstraintList=[]
for i in range(len(Edges)):
    #print("New Edge", Edges[i])
    ConstraintLine=M[i]
    Constraint='subject to Con'+str(i+1)+': '
    for j in range(len(BicliqueSet)):
        if M[i][j]==1:
            Constraint=Constraint+'x['+str(j+1)+']+'
    Constraint=Constraint[:len(Constraint)-1]
    Constraint=Constraint+'=1;'
    ConstraintList.append(Constraint)
    #print(Constraint[:50])
    #print(Constraint[len(Constraint)-20:])
    #print()
'''
'''
with open("constraintfile.txt", "w") as f:
    for line in ConstraintList:
        f.write(f"{line}\n")

with open("edges.txt", "w") as h:
    for edge in Edges:
        x=edge[0]+' <-> '+edge[1]
        h.write(f"{x}\n")
'''