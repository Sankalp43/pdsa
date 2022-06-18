import imp
from bfs import bfsmat
from bfs import neighbours
from bfs import bfslist
from graph import creatematind
from graph import createlisind
from bfs import bfspathlis
from bfs import bfspathlevellis
from dfs import dfslis
from dfs import dfsglobal
from dfs import dfsRecur
from toplog_sort import topSortListQ
from graph import createlisdir
from graph import creatematdir
from toplog_sort import topSortMatNonQ
from longest_pathDAG import longest_path
from graph import weig_Dir_lis
from graph import weig_Dir_Mat
from graph import weig_unDir_lis
from graph import weig_unDir_Mat
from dijkstra import dijkstraList
from dijkstra import dijkstraMat
from belmanford import bellmanfordList
from belmanford import bellmanfordMat
from floyd_warshal import floyd_warshal
from prims import prims
from kruskal import kruskal
from kruskal import kruskalUnionfind
from heaps import Maxheap
from heaps import Minheap
from heap_sort import heap_sort
from Binary_search_tree import Tree
from boyer_moore_algo import boyerMoore
from rabin_karp_algo import rabinkarp
from Trie import Trie
from Trie import SuffixTrie
v = [0,1,2,3,4]  # v -> vertices
e = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]    # e -> list of edges
v1 = [0,1,2,3,4,5,6,7]
e1 = [(0,2),(0,3),(0,4),(1,2),(1,7),(2,5),(3,5),(3,7),(4,7),(5,6),(6,7)]
vw = [0,1,2,3,4,5,6,7]
# ew = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
ew = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]
vw = [0,1,2,3,4]
ew = [(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]



amatud = creatematind(e , v)
alisud = createlisind(e,v)
# print(amatd)
# print(alisd)


b = bfsmat(amatud , 0)
# c = bfslist(alisud , 0)
print(b)
# d , e = bfspathlis(alisud , 0)
# print(c)
# print(d)
# print(e)

# f , g = bfspathlevellis(alisud , 0)
# print(f,g)

# a = {1:'a' , 2:'b' , 3:'c' , 4:'d'}
# # 1
# for i in a:
#     print(i)
# # 2
# for i in a.keys():
#     print(i)


# h = dfslis(alisud , 0)
# print(h)


# i,j = dfsglobal(alisud , 0)
# print(i,j)

# k,l = dfsRecur(alisud , 0)
# print(k , l)

# m = topSortListQ(alisd)
# print(m)

# n = topSortMatNonQ(amatd)
# print(n)

# o = longest_path(alisd)
# print(o)

# wlis = weig_unDir_lis(ew , vw)
# wmat = weig_Dir_Mat(ew , vw)
# print(wmat , wlis)

# shorp = dijkstraMat(wmat,0)
# shorp_ = dijkstraList(wlis,0)
# print(shorp)
# print(shorp_)
 
# shorpneg = bellmanfordMat(wmat , 0)
# shorpneg_ = bellmanfordList(wlis , 0)
# print(shorpneg)
# print(shorpneg_)

# allpairshort = floyd_warshal(wmat)
# print(allpairshort)

# mcst = kruskal(wlis)
# mcst_ = kruskalUnionfind(wlis)
# print(mcst)
# print(mcst_)



# heap = Maxheap()
# heap.build_max_heap([1,2,3,4,5,6])
# print(heap.a)
# heap.insert_in_maxheap(7)
# print(heap.a)
# heap.insert_in_maxheap(8)
# print(heap.a)
# print(heap.delete_max())
# print(heap.delete_max())
# print(heap.a)

# heap = Minheap()
# heap.build_min_heap([6,5,4,3,2])
# print(heap.a)
# heap.insert_in_minheap(1)
# print(heap.a)
# heap.insert_in_minheap(8)
# print(heap.a)
# print(heap.delete_min())
# # print(heap.a)
# print(heap.delete_min())
# print(heap.a)

# A = [8,6,9,3,4,5,61,6666]
# heap_sort(A)
# print(A)

# T = Tree()
# bst = [9,8,7,6,5,4,3,2,1]
# k = 4
# for i in bst:
#     T.insert(i)
# print('Element in BST are:= ',T.inorder())
# print('Maximum element in BST are:= ',T.maxval())
# print('Minimum element in BST are:= ',T.minval())
# print(k,'is present or not = ',T.find(k))
# T.delete(3)
# print('Element in BST after delete 3:= ',T.inorder())

# print(boyerMoore('abcaaacabc','abc'))
# a = rabinkarp('233323233454323','23')
# print(a)
# T = Trie()
# T.add('car')
# T.add('card')
# T.add('care')
# T.add('dog')
# T.add('done')
# # T.add('man')
# T.prin()
# print(T.query('dog'))
# print(T.query('cat'))
# # print(T.query('man'))

# ST = SuffixTrie('card')
# print(ST.root)
# print(ST.followPath('a'))
# print(ST.hasSuffix('aa'))



def BMCount(t , p):
    last = {}
    for i in range(len(p)):
        last[p[i]] = i
        
    i = 0
    poslist = []
    count = 0
    skipl = []
    
    
    while(i<=len(t)-len(p)):
        matched = True
        j = len(p)-1
        
        
            
        while(j>= 0 and matched):
            count +=1
            if(t[i+j] != p[j]):
                 matched = False
                 
            if(p[j] == p[len(p)-1]):
                print(p[j] , p[len(p) - 1])
                skipl.append(i)
                
            
            
            j = j-1
        if(matched):
            poslist.append(i)
            i = i+1
        else:
            j = j+1
            if(t[i+j] in last.keys()):
                i =  i + max(j - last[t[i+j]] , 1)
            else:
                i = i+j+1
        
    return skipl , count
# t = "straw plus berry is strawberry"
# p = "strawberry"                
# print(BMCount(t,p))


def neighbours(graph , node):
    n = []
    for i in range(len(graph[0])):
        if(graph[node][i]) == 1:
            n.append(i)
    return n




from Queue import Queue
def bfs(graph , snode):
    visited = {}
    row,col = len(graph) , len(graph[0])
    for i in range(row):
        visited[i] = False

    q = Queue()
    q.add(snode)

    while(not q.isEmpty()):
        a = q.remove()
        visited[a] = True
        for j in neighbours(graph,a):
            if(not visited[j]):
                q.add(j)

    return visited

print(bfs(amatud , 0))