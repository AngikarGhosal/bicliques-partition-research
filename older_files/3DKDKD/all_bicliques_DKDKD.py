from IPython import embed
from utils import *


with open("3DKDKDBicliques.txt") as file:
    all_bicliques = file.readlines()
    all_bicliques = [line.rstrip() for line in all_bicliques]

#X=obtain_all_tuples_of_nodes(all_bicliques)
#Edges=list(obtain_set_of_unique_edges(X))


#BicliqueSet=list(obtain_all_bicliques(X))

BicliqueSet=obtain_all_tuples_of_nodes(all_bicliques)
Edges=list(obtain_set_of_unique_edges(BicliqueSet))
print(len(BicliqueSet))
print(len(Edges))
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
print(M)
'''
ConstraintList=[]
for i in range(len(Edges)):
    ConstraintLine=M[i]
    Constraint='subject to Con'+str(i+1)+': '
    for j in range(len(BicliqueSet)):
        if M[i][j]==1:
            Constraint=Constraint+'x['+str(j+1)+']+'
    Constraint=Constraint[:len(Constraint)-1]
    Constraint=Constraint+'>=1;'
    ConstraintList.append(Constraint)

with open("coverconstraintfile.txt", "w") as f:
    for line in ConstraintList:
        f.write(f"{line}\n")


with open("bicliques.txt", "w") as g:
    for biclique in BicliqueSet:
        x=biclique[0]+' <-> '+biclique[1]
        g.write(f"{x}\n")

with open("edges.txt", "w") as h:
    for edge in Edges:
        x=edge[0]+' <-> '+edge[1]
        h.write(f"{x}\n")
'''
#embed()

