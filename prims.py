from xmlrpc.client import MAXINT
def prims(Alist):
    infinity = MAXINT
    distance = {}
    visited = {}
    nbr = {}
    for i in Alist:
        visited[i] = False
        distance[i] = infinity
        nbr[i] = -1

    visited[0] = True
    for (v,d) in Alist[0]:
        distance[v] = d
        nbr[v] = 0

    for i in range(1 , len(Alist)):
        nextd = min([distance[i] for i in Alist if not visited[i]])
        nextvlist = [i for i in Alist if not visited[i] and distance[i] == nextd ]
        nextv = min(nextvlist)

        visited[nextv] = True
        for(v,d) in Alist[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v] , d)
                nbr[v] = nextv
    return nbr


    
