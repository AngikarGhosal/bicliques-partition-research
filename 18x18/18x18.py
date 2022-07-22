import numpy as np
M=np.array([[1,1,0],[1,1,1],[0,1,1]])
T=np.array([[1,1],[1,1]])
S=np.array([[1,1],[0,1]])
X=np.kron(M,M)
Y=np.kron(X,T)

print(X)
print(Y)