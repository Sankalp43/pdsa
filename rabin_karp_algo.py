def rabinkarp(t , p):
    poslist = []
    numt = 0
    nump = 0
    for i in range(len(p)):
        numt = numt*10 + int(t[i])
        nump = nump*10 + int(p[i])
    if(numt == nump):
        poslist.append(0)
    
    for i in range(1 , len(t) - len(p) +1):
        numt = numt - int(t[i-1])* (10 ** (len(p)-1))
        numt = numt*10 + int(t[i+len(p)-1])
        if(numt == nump):
            poslist.append(i)
    return poslist
