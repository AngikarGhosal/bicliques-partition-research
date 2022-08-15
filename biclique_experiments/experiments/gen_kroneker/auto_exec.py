from IPython import embed
import os
from glob import glob

lb=3
ub=4
for i in range(lb,ub+1):
    os.system("""python3 sbatch_exec.py -x="train-s" -r="python3 obtain_kroneker.py -V={}" """.format(i))
    #os.system("python3 obtain_kroneker.py -V={}".format(i))
