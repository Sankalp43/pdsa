class UnionFind:
    def __init__(self) -> None:
        self.components = {}
        self.members = {}
        self.size = {}

    def make_Union_Find(self , vertices):
        for vertex in range(vertices):
            self.components[vertex] = vertex
            self.members[vertex] = [vertex]
            self.size[vertex] = 1

    def find(self , vertex):
        return self.components[vertex]
    
    def union(self,u,v):
        c_old = self.components[u]
        c_new = self.components[v]

        if(self.size[c_new]>self.size[c_old]):
            for x in self.members[c_old]:
                self.components[x] = c_new
                self.members[c_new].append(x)
                self.size[c_new] += 1
        else:
            for x in self.members[c_new]:
                self.components[x] = c_old
                self.members[c_old].append(x)
                self.size[c_old] +=1