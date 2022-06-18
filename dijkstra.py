
from xmlrpc.client import MAXINT
import sys


def dijkstraMat(Amat,snode):
    row , col = len(Amat) , len(Amat[0])
    infinity = MAXINT
    visited = {}
    distance = {}
    for i in range(row):
        visited[i] = False
        distance[i] = infinity

    distance[snode] =0 

    for i in range(row):
        nextd = min([distance[v] for v in range(row) if not visited[v]])
        nextdlist = [u for u in range(row) if not visited[u] and distance[u] == nextd]
        nextv = min(nextdlist)

        visited[nextv] = True
        for j in range(col):
            if(Amat[nextv][j][0] == 1) and not visited[j]:
                distance[j] = min(distance[j] , distance[nextv] + Amat[nextv][j][1])
        
    return distance


def dijkstraList(Alist , snode):
    infinity = sys.maxsize
    visited = {}
    distance = {}
    for i in Alist:
        visited[i] = False
        distance[i] = infinity

    distance[snode] = 0

    for i in range(len(Alist)):
        nextd = min([distance[j] for j in Alist if not visited[j]])
        nextdlist = [k for k in Alist if not visited[k] and distance[k] == nextd]
        nextv = min(nextdlist)

        visited[nextv] = True
        for (v,d) in Alist[nextv]:
            if(not visited[v]):
                distance[v] = min(distance[v] , d + distance[nextv])

    return distance





    









# Find shortest path from a vertex to every other vertex.






