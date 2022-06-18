def boyerMoore(t , p):
    last = {}
    for i in range(len(p)):
        last[p[i]] = i
    
    poslist = []
    i = 0
    while(i<= len(t) - len(p)):
        matched = True
        j = len(p) - 1
        while(j>=0 and  matched):
            if(t[i+j] != p[j]):
                matched = False
            j = j-1

        if(matched):
            poslist.append(i)
            i = i+1
        else:
            j = j+1
            if(t[i+j] in last.keys()):
                i = i + max(j-last[t[i+j]] , 1)

            else:
                i = i+j+1
    return poslist
