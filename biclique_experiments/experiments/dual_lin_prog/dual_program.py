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
import cvxpy as cp
import sys
np.set_printoptions(threshold=sys.maxsize)


parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, default='../../datafiles/Constraints/3DKDconstraints.npy', help='constraints file path')
parser.add_argument('--program', type=str, default='cont_part', help='kind of program to run')
args = parser.parse_args()
filepath=args.filename
program=args.program
print(filepath)
print(program)
#print(filepath[28:-15])
Mx=np.load(filepath, allow_pickle=True)

c=np.array([1 for i in range(Mx.shape[1])])
integrality_d=np.array([1 for i in range(Mx.shape[1])])
integrality_c=np.array([0 for i in range(Mx.shape[1])])
bounds=(0,1)

A_eq=Mx
print(Mx.shape)
Eye=np.eye(Mx.shape[0])
ones=np.ones(Mx.shape[0])
zeros=np.zeros(Mx.shape[0])

if program=='cont_part':
    d=np.array([1 for i in range(Mx.shape[0])])
    y = cp.Variable(Mx.shape[0])
    b_new=b_eq=np.array([1 for i in range(Mx.shape[1])])
    prob = cp.Problem(cp.Maximize(d.T@y), [A_eq.T @ y <= b_new])
    prob.solve(verbose=True)
    ans=prob.value

elif program=='cont_cover':
    d=np.array([1 for i in range(Mx.shape[0])])
    y = cp.Variable(Mx.shape[0])
    b_new=b_eq=np.array([1 for i in range(Mx.shape[1])])
    prob = cp.Problem(cp.Maximize(d.T@y), [A_eq.T @ y <= b_new, y>=zeros])
    prob.solve(verbose=True)
    ans=prob.value

if program=='integer_part':
    d=np.array([1 for i in range(Mx.shape[0])])
    y = cp.Variable(Mx.shape[0], integer=True)
    b_new=b_eq=np.array([1 for i in range(Mx.shape[1])])
    prob = cp.Problem(cp.Maximize(d.T@y), [A_eq.T @ y <= b_new])
    prob.solve(verbose=True)
    ans=prob.value

elif program=='integer_cover':
    d=np.array([1 for i in range(Mx.shape[0])])
    y = cp.Variable(Mx.shape[0], integer=True)
    b_new=b_eq=np.array([1 for i in range(Mx.shape[1])])
    prob = cp.Problem(cp.Maximize(d.T@y), [A_eq.T @ y <= b_new, y>=zeros])
    prob.solve(verbose=True)
    ans=prob.value

elif program=='bool_part':
    d=np.array([1 for i in range(Mx.shape[0])])
    y = cp.Variable(Mx.shape[0], boolean=True)
    b_new=b_eq=np.array([1 for i in range(Mx.shape[1])])
    prob = cp.Problem(cp.Maximize(d.T@y), [A_eq.T @ y <= b_new])
    prob.solve(verbose=True)
    ans=prob.value

elif program=='bool_cover':
    d=np.array([1 for i in range(Mx.shape[0])])
    y = cp.Variable(Mx.shape[0], boolean=True)
    b_new=b_eq=np.array([1 for i in range(Mx.shape[1])])
    prob = cp.Problem(cp.Maximize(d.T@y), [A_eq.T @ y <= b_new, y>=zeros])
    prob.solve(verbose=True)
    ans=prob.value


# Print result.
print("\nThe optimal value is", ans)
print("A solution y is")
print(y.value)
for i in range(len(y.value)):
    if (y.value)[i]>0.01 or (y.value)[i]<-0.01:
        print(i, (y.value)[i])

print("DUAL")
print(prob.constraints[0].dual_value)
print("DUAL OVER")
