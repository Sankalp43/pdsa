from Union_Find import UnionFind


def kruskal(Alist):
    edge = []
    component = {}
    te = []

    for u in Alist.keys():
        for (v,d) in Alist[u]:
            z = (d,u,v)
            edge.append(z)
        
        component[u] = u
    edge.sort()                                 # complexity O(n**2)

    for(d,u,v) in edge:
        if(component[u] != component[v]):
            te.append((u,v))
        c = component[u]
        for w in Alist.keys():
            if(component[w] == c):
                component[w] = component[v]
    return te



def kruskalUnionfind(Alist):
    edge = []
    te = []

    uf = UnionFind()
    uf.make_Union_Find(len(Alist))

    for u in Alist.keys():
        for (v,d) in Alist[u]:
            z = (d,u,v)
            edge.append(z)
    edge.sort()                                # complexity O((m+n)logn)

    for (d,u,v) in edge:
        if uf.components[u] != uf.components[v]:
            te.append((u,v))
            uf.union(u,v)
    
    return te









        

