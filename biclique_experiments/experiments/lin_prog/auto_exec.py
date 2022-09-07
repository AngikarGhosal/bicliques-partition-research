import os
import glob

programs=['disc_cover', 'disc_part', 'frac_cover', 'frac_part', 'half_part']
files=glob.glob('../../datafiles/Constraints/**/*.npy', recursive=True)
nfiles=['../../datafiles/Constraints/DKDconstraints.npy','../../datafiles/Constraints/DKDKDconstraints.npy']
for f in nfiles:
    for prog in programs:
        os.system("""python3 sbatch_exec.py -x="train-s" -r="python3 new_linearprogramming.py --filename={} --program={}" """.format(f, prog))
        #os.system("python3 new_linearprogramming.py --filename={} --program={}".format(f, prog))
