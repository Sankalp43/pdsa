from Stack import Stack


def dfslis(Alis , snode):
    visited = {}
    for i in Alis:
        visited[i] = False

    s = Stack()
    s.add(snode)
    

    while(not s.is_Empty()):
        a = s.remove()
        if(not visited[a]):
            visited[a] = True

        for j in Alis[a]:
            if(not visited[j]):
                s.add(j)

    return visited


def dfsglobal(Alist , snode):
    visited = {}
    parent = {}

    def dfsInitListGlobal(Alist):
        for i in Alist:
            visited[i] = False
            parent[i] = -1
        return

    def dfsListGlobal(Alist , snode):
        visited[snode] = True
        for j in Alist[snode]:
            if(not visited[j]):
                parent[j] = snode
                dfsListGlobal(Alist , j)
        return
    
    dfsInitListGlobal(Alist)
    dfsListGlobal(Alist , snode)
    return visited , parent





def dfsRecur(Alist , snode):
    def dfsInit(Alist):
        visited = {}
        parent = {}
        for i in Alist:
            visited[i] = False
            parent[i] = -1
        return visited , parent

    def dfsList(Alist , snode , visited , parent):
        visited[snode] =True
        for j in Alist[snode]:
            if(not visited[j]):
                parent[j] = snode
                visited,parent = dfsList(Alist , j , visited , parent)
        return visited , parent

    visited , parent = dfsInit(Alist)
    v , p = dfsList(Alist , snode , visited , parent)
    return v,p