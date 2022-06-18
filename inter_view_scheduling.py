def tuplesort(L, index):
    L_ = []
    for t in L:
        # print(t[index:index+1] , t[:index] , t[index+1:])
        # print(t[index:index+1] + t[:index] + t[index+1:])
        L_.append(t[index:index+1] + t[:index])
    L_.sort()
    # print(L_)


    L__ = []
    for t in L_:
        # print(t[1:index+1] , t[0:1] , t[index+1:])
        # print(t[1:index+1] + t[0:1] + t[index+1:])
        L__.append(t[1:index+1] + t[0:1])
    # print(L__)
    return L__

# sortedL = tuplesort(L, 2)
    
def intervalschedule(L):
    sortedL = tuplesort(L, 2)
    # print(sortedL)
    accepted = [sortedL[0][0]]
    # print(accepted)
    # print(sortedL[1:])
    for i, s, f in sortedL[1:]:
        # print(accepted[-1] , L[accepted[-1]])
        if s > L[accepted[-1]][2]:
            accepted.append(i)
    return accepted

# L = [(0, 1, 2),(1, 1, 3),(2, 1, 5),(3, 3, 4),(4, 4, 5),(5, 5, 8),(6, 7, 9),(7, 10, 13),(8, 11, 12)]

# print(intervalschedule(L))
