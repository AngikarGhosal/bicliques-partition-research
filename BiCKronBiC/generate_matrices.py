from utils import *
import numpy as np
N=3

def process_left_node(x):
    a=int(x)
    return a-1

def process_right_node(x):
    b=int(x)
    return (b-N-1)

def obtain_biclique_string_from_matrix(M):
    Z=np.nonzero(M)
    xcoords=Z[0]
    ycoords=Z[1]
    for i in range(len(xcoords)):
        xcoords[i]=(xcoords[i]+1)
    for i in range(len(ycoords)):
        ycoords[i]=(ycoords[i]+1+N*N)
    xcoords=sorted(list(set(xcoords)))
    ycoords=sorted(list(set(ycoords)))
    for i in range(len(xcoords)):
        xcoords[i]=str(xcoords[i])
    for i in range(len(ycoords)):
        ycoords[i]=str(ycoords[i])
    xstr=' '.join(xcoords)
    ystr=' '.join(ycoords)
    ans=xstr+' <-> '+ystr 
    return ans


with open('3domino_bicliques.txt') as my_file:
    lines = my_file.readlines()
    lines = [line.rstrip() for line in lines]

all_biclique_tuples=obtain_all_tuples_of_nodes(lines)

list_of_sets_of_edges=[]
for tuple in all_biclique_tuples:
    set_of_edge_tuples=obtain_set_of_edges_from_biclique(*tuple)
    list_of_sets_of_edges.append(set_of_edge_tuples)

list_of_matrices=[]
for set_of_edges in list_of_sets_of_edges:
    matrix=np.array([[0 for i in range(N)] for j in range(N)])
    for tuple in set_of_edges:
        a,b=process_left_node(tuple[0]),process_right_node(tuple[1])
        matrix[a,b]=1
    list_of_matrices.append(matrix)

set_of_kroneker_triples=[]
for X in list_of_matrices:
    set_of_kroneker_triples.append((X,X,np.kron(X,X)))

for i in range(len(list_of_matrices)):
    for j in range(i+1, len(list_of_matrices)):
        set_of_kroneker_triples.append((list_of_matrices[i],list_of_matrices[j],np.kron(list_of_matrices[i],list_of_matrices[j])))

list_of_kron_bicliques=[]

for i in range(len(set_of_kroneker_triples)):
    string=obtain_biclique_string_from_matrix(set_of_kroneker_triples[i][2])
    list_of_kron_bicliques.append(string)
import csv
resultFile = open("BicKronBic.txt",'w')

# Write data to file
for r in list_of_kron_bicliques:
    resultFile.write(r + "\n")
resultFile.close()

