from IPython import embed
import numpy as np
import argparse
from pathlib import Path
import os
import pandas as pd
import scipy as sp
import scipy.optimize as sop
import pickle
from pickle_func import *
import sys
import cvxpy as cp
np.set_printoptions(threshold=sys.maxsize)
Path("../../datafiles/LinearProgramming").mkdir(parents=True, exist_ok=True)

Path("../../datafiles/LinearProgramming/FractionalCover").mkdir(parents=True, exist_ok=True)
Path("../../datafiles/LinearProgramming/FractionalPartition").mkdir(parents=True, exist_ok=True)
Path("../../datafiles/LinearProgramming/DiscreteCover").mkdir(parents=True, exist_ok=True)
Path("../../datafiles/LinearProgramming/DiscretePartition").mkdir(parents=True, exist_ok=True)
Path("../../datafiles/LinearProgramming/HalfPartition").mkdir(parents=True, exist_ok=True)

frac_cover_path="../../datafiles/LinearProgramming/FractionalCover/"
frac_part_path="../../datafiles/LinearProgramming/FractionalPartition/"
disc_cover_path="../../datafiles/LinearProgramming/DiscreteCover/"
disc_part_path="../../datafiles/LinearProgramming/DiscretePartition/"
half_part_path="../../datafiles/LinearProgramming/HalfPartition/"

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, default='../../datafiles/Constraints/DKDconstraints.npy', help='constraints file path')
parser.add_argument('--program', type=str, default='disc_part', help='kind of program to run')
args = parser.parse_args()
filepath=args.filename
program=args.program
print(filepath)
print(program)
Z=filepath[28:-15]+'base'
Mx=np.load(filepath, allow_pickle=True)

c=np.array([1 for i in range(Mx.shape[1])])
integrality_d=np.array([1 for i in range(Mx.shape[1])])
integrality_c=np.array([0 for i in range(Mx.shape[1])])
bounds=(0,1)
A_eq=Mx
b_eq=np.array([1 for i in range(Mx.shape[0])])
print(Mx.shape)
Eye=np.eye(Mx.shape[1])
ones=np.ones(Mx.shape[1])
zeros=np.zeros(Mx.shape[1])


if program=='disc_cover':
    x = cp.Variable(Mx.shape[1], boolean=True)
    prob = cp.Problem(cp.Minimize(c.T@x), [A_eq @ x >= b_eq])
    prob.solve(verbose=True)
    ans=prob.value
    filenamepath=disc_cover_path+Z+"results.txt"
    with open(filenamepath, "w") as f:
        print_to_file(f,ans,x,prob,program)
elif program=='disc_part':
    x = cp.Variable(Mx.shape[1], boolean=True)
    prob = cp.Problem(cp.Minimize(c.T@x), [A_eq @ x == b_eq])
    prob.solve(verbose=True)
    ans=prob.value
    filenamepath=disc_part_path+Z+"results.txt"
    with open(filenamepath, "w") as f:
        print_to_file(f,ans,x,prob,program)
elif program=='frac_cover':
    x = cp.Variable(Mx.shape[1])
    prob = cp.Problem(cp.Minimize(c.T@x), [A_eq @ x >= b_eq, Eye @ x >= zeros, Eye @ x <= ones])
    prob.solve(verbose=True)
    ans=prob.value
    filenamepath=frac_cover_path+Z+"results.txt"
    with open(filenamepath, "w") as f:
        print_to_file(f,ans,x,prob,program)
elif program=='frac_part':
    x = cp.Variable(Mx.shape[1])
    prob = cp.Problem(cp.Minimize(c.T@x), [A_eq @ x == b_eq, Eye @ x >= zeros, Eye @ x <= ones])
    prob.solve(verbose=True)
    ans=prob.value
    filenamepath=frac_part_path+Z+"results.txt"
    with open(filenamepath, "w") as f:
        print_to_file(f,ans,x,prob,program)
elif program=='half_part':
    twos=ones*2
    b_two=b_eq*2
    x = cp.Variable(Mx.shape[1], integer=True)
    prob = cp.Problem(cp.Minimize(c.T@x), [A_eq @ x == b_two, Eye @ x >= zeros, Eye @ x <= twos])
    prob.solve(verbose=True)
    ans=(prob.value)/2
    filenamepath=half_part_path+Z+"results.txt"
    with open(filenamepath, "w") as f:
        print_to_file(f,ans,x,prob,program)




print("DUAL")
print(prob.constraints[0].dual_value)
print("DUAL OVER")
y=[i for i in x.value]
if program=='half_part':
    for i in range(len(y)):
        y[i]=y[i]/2

# Print result.
print("\nThe optimal value is", ans)
print("A solution x is")
print(x.value)
for i in range(len(x.value)):
    if (x.value)[i]>0.01:
        print(i, (x.value)[i])


