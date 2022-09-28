import os
import glob

f_list=glob.glob('../../datafiles/AllBicliques/**/*.txt', recursive=True)
g_list=glob.glob('../../datafiles/Edges/**/*.txt', recursive=True)
assert (len(f_list)==len(g_list))
for i in range(len(f_list)):
    f_name=f_list[i][29:-16]
    g_name=g_list[i][22:-9]
    assert(f_name==g_name)
    os.system("""python3 sbatch_exec.py -x="train-s" -r="python3 constraints.py --bicfile={} --edgefile={}" """.format(f_list[i],g_list[i]))
    #os.system("python3 constraints.py --bicfile={} --edgefile={}".format(f_list[i],g_list[i]))

