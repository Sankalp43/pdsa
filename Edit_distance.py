import numpy as np

def eD(a , b):
    m = len(a)
    n = len(b)
    
    ed = np.zeros((m+1 , n+1))
    for i in range(m-1 , -1 , -1):
        ed[i,n] = m-i
    for j in range(n-1 , -1 , -1):
        ed[j, m] = n-i


    for j in range(n-1 , -1 , -1):
        for i in range(m-1 , -1 , -1):
            if (a[i] == b[j]):
                ed[i,j] = ed[i+1 , j+1]
            else:
                ed[i,j] = 1 + min(ed[i+1 , j] , ed[i , j+1] , ed[i+1 , j+1])
    return ed[0,0]
