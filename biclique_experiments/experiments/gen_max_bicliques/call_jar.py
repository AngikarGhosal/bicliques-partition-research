import os
from pathlib import Path
import argparse
Path("../../datafiles/Bicliques").mkdir(parents=True, exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='../../datafiles/Matrices/3DKDMatrix.txt', help='matrix file path')

args = parser.parse_args()
file_path=args.file

matrixtype=file_path[20:-10]
biclique_path='../../datafiles/Bicliques/'+matrixtype+'Bicliques.txt'
os.system("""java -jar MBEA.jar {} standard > {}""".format(file_path, biclique_path))



    