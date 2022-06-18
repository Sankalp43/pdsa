import numpy as np
def lCSS(a , b):
    m = len(a)
    n = len(b)
    lcss = np.zeros((m+1 , n+1))

    for j in range(m-1 , -1 , -1):
        for i in range(n-1, -1, -1):
            if(a[j] == b[i]):
                lcss[i,j] = 1 + lcss[i+1 , j+1]
            else:
                lcss[i,j] = max(lcss[i,j+1] , lcss[i+1 , j])

    return lcss[0,0]