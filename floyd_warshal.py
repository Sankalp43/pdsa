import sys
from xmlrpc.client import MAXINT
import numpy as np
def floyd_warshal(Amat):
    row , col = len(Amat) , len(Amat[0])
    # infinity = MAXINT//100000
    infinity = np.max(Amat)*row*row+1
   

    sp = np.zeros((row , col , col+1) , dtype=int)
    for i in range(row):
        for j in range(col):
            sp[i][j][0] = infinity

    for i in range(row):
        for j in range(col):
            if(Amat[i][j][0] == 1):
                sp[i][j][0] = Amat[i][j][1]
    
    for k in range(1,col+1):
        for i in range(row):
            for j in range(col):
                sp[i,j,k] = min(sp[i,j,k-1] , sp[i,k-1,k-1] + sp[k-1 , j , k-1])

    return sp[:,:,col]
