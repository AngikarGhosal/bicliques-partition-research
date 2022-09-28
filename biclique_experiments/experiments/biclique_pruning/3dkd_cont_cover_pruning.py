from IPython import embed
from utils import *
import numpy as np
import argparse
from pathlib import Path
import os
parser = argparse.ArgumentParser()
parser.add_argument('--bicfile', type=str, default='../../datafiles/Bicliques/DKDBicliques.txt', help='all bicliques file path')
parser.add_argument('--edgefile', type=str, default='../../datafiles/Edges/DKDedges.txt', help='all edges file path')
parser.add_argument('--savefile', type=str, default='../../datafiles/SmartBicliques/DKDSmartBicliques.txt', help='where the smart bicliques get stored')
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


[ 3.70369532e-02, -1.85184563e-02,  3.70369623e-02,  3.70369568e-02,
  6.48147382e-02,  3.70369583e-02,  6.48147313e-02,  6.48147340e-02,
  6.48147338e-02,  3.70369616e-02, -1.85184457e-02, -7.40739925e-02,
  6.48147404e-02,  3.70369632e-02,  2.74968086e-07,  6.48147390e-02,
  6.48147339e-02, -1.85184789e-01, -7.40739986e-02,  3.70369611e-02,
 -1.85184263e-02,  3.70369636e-02,  3.70369649e-02,  6.48147224e-02,
  6.48147364e-02, -7.40739883e-02, -1.85184562e-02, -7.40739945e-02,
 -1.85184203e-02,  3.70369621e-02,  6.48147419e-02,  6.48147366e-02,
  3.70369569e-02, -1.85184302e-02,  6.48147324e-02,  3.70369631e-02,
  2.71463161e-07,  2.78596588e-07,  3.70369563e-02,  3.70369655e-02,
  3.70369592e-02,  6.48147348e-02,  6.48147353e-02, 6.48147393e-02,
  2.78341621e-07,  6.48147403e-02,  3.70369615e-02, -1.85184223e-02,
 -1.85184226e-02]

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
