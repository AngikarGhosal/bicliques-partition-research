from IPython import embed
from utils import *
import numpy as np
import argparse
from pathlib import Path
import os
Path("../../datafiles/Constraints").mkdir(parents=True, exist_ok=True)
constraint_folder="../../datafiles/Constraints/"
parser = argparse.ArgumentParser()
parser.add_argument('--bicfile', type=str, default='../../datafiles/Bicliques/DKDKDBicliques.txt', help='all bicliques file path')
parser.add_argument('--edgefile', type=str, default='../../datafiles/Edges/DKDKDedges.txt', help='all edges file path')
args = parser.parse_args()
bicfile_path=args.bicfile
edgefile_path=args.edgefile
print(bicfile_path[26:-13])

with open(bicfile_path, 'r') as bicfilename:
    all_bicliques = bicfilename.readlines()
    all_bicliques = [line.rstrip() for line in all_bicliques]
bicfilename.close()

with open(edgefile_path, 'r') as edgefilename:
    all_edges = edgefilename.readlines()
    all_edges = [line.rstrip() for line in all_edges]
edgefilename.close()

all_biclique_tuples=[]
all_edge_tuples=[]

for i in all_bicliques:
    all_biclique_tuples.append(obtain_tuple_of_first_and_second_nodes(i))

for i in all_edges:
    all_edge_tuples.append(obtain_tuple_of_first_and_second_nodes(i))
print(all_biclique_tuples[2360:])
M=[[0 for i in range(len(all_biclique_tuples))] for j in range(len(all_edge_tuples))]

for i in range(len(all_biclique_tuples)):
    List_of_Edges=list(obtain_set_of_edges_from_biclique(*(all_biclique_tuples[i])))
    L0=all_biclique_tuples[i][0].split(" ")
    L1=all_biclique_tuples[i][1].split(" ")
    for edge in List_of_Edges:
        edge_position=all_edge_tuples.index(edge)
        if edge[0] in L0 and edge[1] in L1:
            M[edge_position][i]=1        
save_path=constraint_folder+bicfile_path[26:-13]+"constraints.npy"
Mx=np.array(M)
np.save(save_path, Mx)
print(Mx.shape)
new_save_path=constraint_folder+bicfile_path[26:-13]+"constraints.txt"
with open(new_save_path, "w") as f:
    for line in M:
        for i in range(len(line)):
            line[i]=str(line[i])
        V=" ".join(line)
        f.write(f"{V}\n")
