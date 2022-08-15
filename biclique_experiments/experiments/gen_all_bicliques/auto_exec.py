import os
import glob

for f in glob.glob('../../datafiles/Bicliques/**/*.txt', recursive=True):
    os.system("""python3 sbatch_exec.py -x="train-s" -r="python3 all_bicliques.py --file={}" """.format(f))
    #os.system("python3 all_bicliques.py --file={}".format(f))
