from IPython import embed
from utils import *
import numpy as np
import argparse
from pathlib import Path
import os
parser = argparse.ArgumentParser()
parser.add_argument('--bicfile', type=str, default='../../datafiles/SmartBicliques/3DKDSmartBicliques.txt', help='all bicliques file path')
parser.add_argument('--edgefile', type=str, default='../../datafiles/Edges/3DKDedges.txt', help='all edges file path')
parser.add_argument('--savefile', type=str, default='../../datafiles/SmartBicliques/3DKDSmartSmartBicliques.txt', help='where the smart bicliques get stored')
args = parser.parse_args()
bicfile_path=args.bicfile
edgefile_path=args.edgefile
savefile_path=args.savefile

with open(bicfile_path, 'r') as bicfilename:
    all_bicliques = bicfilename.readlines()
    all_bicliques = [line.rstrip() for line in all_bicliques]
bicfilename.close()

with open(edgefile_path, 'r') as edgefilename:
    all_edges = edgefilename.readlines()
    all_edges = [line.rstrip() for line in all_edges]
edgefilename.close()

edges_dict={0: 0.5, 3:-0.5, 4:0.5, 5:0.5, 6:-0.5, 11:0.5, 12:0.5, 16:-0.5, 22:0.5, 25:0.5, 28:0.5, 36:0.5, 
39:0.5, 40:0.5, 41:0.5, 42:-0.5, 43:0.5, 45:0.5, 46:0.5, 47:0.5}

#print(all_bicliques[:10])
#print(all_edges[:10])

good_edges=[]
bad_edges=[]
for edgeno in edges_dict.keys():
    if edges_dict[edgeno]==0.5:
        good_edges.append(all_edges[edgeno])
    else:
        bad_edges.append(all_edges[edgeno])

print("3DKD")
new_bicliques=[]
for biclique in all_bicliques:
    for bad_edge in bad_edges:
        if check_edge_in_biclique(bad_edge, biclique):
            for good_edge in good_edges:
                if check_edge_in_biclique(good_edge, biclique):
                    if check_edges_not_common(good_edge, bad_edge):
                        new_biclique=remove_bad_vertices(biclique, bad_edge)
                        if new_biclique!=-1:
                            new_bicliques.append(new_biclique)
                            print("NEW BICLIQUE")
                            print(new_biclique)
                            print("OLD BICLIQUE")
                            print(biclique)
                            print("GOOD_EDGE")
                            print(good_edge)
                            print("BAD_EDGE")
                            print(bad_edge)
                            print("\n\n")



with open(savefile_path, "w") as h:
    for nb in new_bicliques:
        h.write(f"{nb}\n")
