import numpy as np
def lCSW(a,b):
    m = len(a)
    n = len(b)
    lcw = np.zeros((m+1 , n+1) )
    maxlcsw = 0

    for i in range(n-1 , -1 , -1):
        for j in range(m-1 , -1 , -1):
            if b[i] == a[j]:
                lcw[j , i] = 1 + lcw[i+1 , j+1]
            else:
                lcw[j,i] = 0
            if(lcw[j,i]>maxlcsw):
                maxlcsw = lcw[i,j]

    return maxlcsw

