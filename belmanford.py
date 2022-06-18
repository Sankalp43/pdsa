import sys
def bellmanfordMat(Amat,s):
    infinity = sys.maxsize
    distance= {}
    row,col = len(Amat) , len(Amat[0])
    for i in range(row):
        distance[i] = infinity
    distance[s] = 0
    for i in range(row):
        for u in range(row):
            for v in range(col):
                if(Amat[u][v][0] == 1):
                    distance[v] = min(distance[v], distance[u] + Amat[u][v][1])
    return distance




def bellmanfordList(Alist,s):
    infinity = sys.maxsize
    distance = {}
    for i in Alist:
        distance[i] = infinity
    distance[s] = 0
    for i in Alist:
        for u in Alist:
            for (v,d) in Alist[u]:
                distance[v] = min(distance[v] , distance[u] + d)
    return distance
