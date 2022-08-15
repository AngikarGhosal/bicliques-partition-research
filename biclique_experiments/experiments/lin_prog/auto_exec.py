import os
import glob

programs=['disc_cover', 'disc_part', 'frac_cover', 'frac_part', 'half_part']
files=glob.glob('../../datafiles/Constraints/**/*.npy', recursive=True)
nfiles=['../../datafiles/Constraints/3DKDconstraints.npy']
for f in files:
    for prog in programs:
        os.system("""python3 sbatch_exec.py -x="train-s" -r="python3 linearprogramming.py --filename={} --program={}" """.format(f, prog))
        #os.system("python3 linearprogramming.py --filename={} --program={}".format(f, prog))
