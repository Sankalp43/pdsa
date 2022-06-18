from Queue import Queue


def topSortMatNonQ(Amat): 
    def indegree(Amat):
        ind = {}
        row , col = len(Amat) , len(Amat[0])
        for i in range(col):
            ind[i] = 0
            for j in range(row):
                if(Amat[j][i]==1):
                    ind[i] = ind[i]+1
        return  ind

    # Without using Queue



    def topsort(Amat):                
        row , col = len(Amat) , len(Amat[0])
        topsortlis = []
        indegre = indegree(Amat)
        for i in range(row):
            a = min([j for j in indegre if indegre[j] == 0])
            topsortlis.append(a)
            indegre[a] = indegre[a] -1
            for k in range(col):
                if(Amat[i][k]==1):
                    indegre[k] = indegre[k]-1
        return topsortlis

    return topsort(Amat)


def topSortListQ(Alist):

    def indegree(Alist):
        ind = {}
        for i in Alist:
            ind[i] = 0

        for i in Alist:
            for j in Alist[i]:
                ind[j] = ind[j]+1
        return  ind

     # With Queue

    def topsort(Alist):
        topsortlis = []
        indegre = indegree(Alist)
        zerodegQ = Queue()
        for u in Alist:
            if indegre[u] == 0:
                zerodegQ.add(u)

        

        while(not zerodegQ.isEmpty()):
            j = zerodegQ.remove()
            topsortlis.append(j)
            # indegre[j] = indegre[j] -1
            for i in Alist[j]:
                indegre[i] = indegre[i] - 1
                if(indegre[i] == 0):
                    zerodegQ.add(i)
        return topsortlis

    return topsort(Alist)








