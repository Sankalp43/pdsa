from Queue import Queue

def neighbours(graph , node):
    n = []
    for i in range(len(graph[0])):
        if(graph[node][i]) == 1:
            n.append(i)
    return n





def bfsmat(graph , snode):
    visited = {}
    row,col = len(graph) , len(graph[0])
    for i in range(row):
        visited[i] = False
    

    q = Queue()
    q.add(snode)
    visited[snode] = True

    while(not q.isEmpty()):
        a = q.remove()
        
        for j in neighbours(graph,a):
            if(not visited[j]):
                visited[j] = True
                q.add(j)

    return visited


def bfslist(graph , snode):
    visited = {}
    for i in graph:
        visited[i] = False

    q = Queue()
    q.add(snode)
    visited[snode] = True
    while(not q.isEmpty()):
        a = q.remove()
        for j in graph[a]:
            if(not visited[j]):
                visited[j] = True
                q.add(j)

    return visited

        
        
def bfspathlis(Alis , snode):
    visited = {}
    parent = {}
    for i in Alis:
        visited[i] = False
        parent[i] = -1
    q = Queue()
    q.add(snode)
    visited[snode] = True

    while(not q.isEmpty()):
        a = q.remove()
        for j in Alis[a]:
            if(not visited[j]):
                visited[j] = True
                parent[j] = a
                q.add(j)
            
    return visited , parent
    
def bfspathlevellis(Alis,snode):
    level = {}
    parent = {}

    for i in Alis:
        level[i] = -1
        parent[i] = -1

    level[snode] = 0
    q = Queue()
    q.add(snode)

    while(not q.isEmpty()):
        a = q.remove()
        for j in Alis[a]:
            if(level[j]==-1):
                level[j] = level[a]+1
                parent[j] = a
                q.add(j)

    return level , parent