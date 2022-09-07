import os
import glob

programs=['cont_part', 'cont_cover', 'integer_part', 'integer_cover', 'bool_part', 'bool_cover']
files=glob.glob('../../datafiles/Constraints/**/*.npy', recursive=True)
nfiles=['../../datafiles/Constraints/DKDconstraints.npy', '../../datafiles/Constraints/DKDKDconstraints.npy']
for f in nfiles:
    for prog in programs:
        os.system("""python3 sbatch_exec.py -x="train-s" -r="python3 new_dual_program.py --filename={} --program={}" """.format(f, prog))
        #os.system("python3 dual_program.py --filename={} --program={}".format(f, prog))
