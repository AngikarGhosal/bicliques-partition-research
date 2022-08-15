from IPython import embed
from utils import *
all_bicliques=['1 2 4 5 <-> 10 11 13 14','2 5 <-> 10 11 13 14 12 15','5 <-> 10 11 13 14 12 15 16 17 18','4 5 <-> 10 11 13 14 16 17',
'1 2 3 4 5 6 <-> 11 14','2 3 5 6 <-> 11 14 12 15','5 6 <-> 11 14 12 15 17 18','4 5 6 <-> 11 14 17','1 2 4 5 7 8 <-> 13 14','2 5 8 <-> 13 14 15',
'5 8 <-> 13 14 15 16 17 18','4 5 7 8 <-> 13 14 16 17','1 2 3 4 5 6 7 8 9 <-> 14','2 3 5 6 8 9 <-> 14 15','5 6 8 9 <-> 14 15 17 18',
'4 5 6 7 8 9 <-> 14 17']
with open("BicKronBic.txt") as file:
    BKB_bicliques = file.readlines()
    BKB_bicliques = [line.rstrip() for line in BKB_bicliques]

X=obtain_all_tuples_of_nodes(all_bicliques)
Edges=list(obtain_set_of_unique_edges(X))
BicliqueSet=list(obtain_all_bicliques(X))
BKBSet=obtain_all_tuples_of_nodes(BKB_bicliques)

print(len(BKBSet))


M=[[0 for i in range(len(BKBSet))] for j in range(len(Edges))]

for i in range(len(BKBSet)):
    List_of_Edges=list(obtain_set_of_edges_from_biclique(*(BKBSet[i])))
    L0=BKBSet[i][0].split(" ")
    L1=BKBSet[i][1].split(" ")
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

ConstraintList=[]
for i in range(len(Edges)):
    #print("New Edge", Edges[i])
    ConstraintLine=M[i]
    Constraint='subject to Con'+str(i+1)+': '
    for j in range(len(BKBSet)):
        if M[i][j]==1:
            Constraint=Constraint+'x['+str(j+1)+']+'
    Constraint=Constraint[:len(Constraint)-1]
    Constraint=Constraint+'=1;'
    ConstraintList.append(Constraint)

with open("new_constraintfile.txt", "w") as f:
    for line in ConstraintList:
        f.write(f"{line}\n")


with open("new_bicliques.txt", "w") as g:
    for biclique in BKBSet:
        x=biclique[0]+' <-> '+biclique[1]
        g.write(f"{x}\n")

with open("new_edges.txt", "w") as h:
    for edge in Edges:
        x=edge[0]+' <-> '+edge[1]
        h.write(f"{x}\n")

#embed()

