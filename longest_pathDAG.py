from Queue import Queue

def longest_path(Alist):
    path = {}
    indegre = {}
    zerodegQ = Queue()

    for i in Alist:
        path[i] = 0
        indegre[i] = 0

    for u in Alist:
        for v in Alist[u]:
            indegre[v] = indegre[v] +1
        
    for j in Alist:
        if indegre[j] == 0:
            zerodegQ.add(j)

    while(not zerodegQ.isEmpty()):
        k = zerodegQ.remove()
        
        for j in Alist[k]:
            indegre[j] = indegre[j] -1
            path[j] = max(path[j] , path[k] +1)
            if indegre[j] == 0:
                zerodegQ.add(j)

    return path 