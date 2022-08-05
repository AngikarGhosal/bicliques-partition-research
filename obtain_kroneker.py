import numpy as np

def Domino(N):
    S=[[0 for i in range(N)] for j in range(N)]
    S[0][0]=1
    S[0][1]=1
    S[N-1][N-1]=1
    S[N-1][N-2]=1
    for i in range(1,N-1):
        S[i][i-1]=1
        S[i][i]=1
        S[i][i+1]=1
    return S

def DominoKronekerDomino(N):
    S=Domino(N)
    X=np.kron(S,S)
    X=X.tolist()
    return X

def DKDKD(N):
    S=Domino(N)
    X=np.kron(S,S)
    Y=np.kron(X,S)
    Y=Y.tolist()
    return Y


VAL=3
#X=DominoKronekerDomino(VAL)
Y=DKDKD(VAL)
filename=str(VAL)+"DKDKDMatrix.txt"
with open(filename, "w") as f:
    for line in Y:
        for i in range(len(line)):
            line[i]=str(line[i])
        V=" ".join(line)
        print(V)
        f.write(f"{V}\n")

