import os
import glob

for f in glob.glob('../../datafiles/Matrices/**/*.txt', recursive=True):
    os.system("""python3 sbatch_exec.py -x="train-s" -r="python3 call_jar.py --file={}" """.format(f))
    #os.system("python3 call_jar.py --file={}".format(f))
