import numpy as np
# For directed Graphs.

v = [0,1,2,3,4]  # v -> vertices
e = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]    # e -> list of edges

# Adjancey matrix using numpy.

size = len(v)
from venv import create

amat = np.zeros((size,size) , dtype=int)
for (i,j) in e:
    amat[i,j] = 1
# print(amat)


# adjancey matrix using nested list.
def creatematdir(e,v):
    Amat1 = []
    size = len(v)
    for i in range(size):      # for row
        row = []
        for i in range(size):    # for col
            row.append(0)
        Amat1.append(row)

    for (i,j) in e:
        Amat1[i][j] = 1
    return Amat1

# Adjancey list using dictionary
def createlisdir(e,v):
    size = len(v)
    Alist = {}
    for i in range(size):
        Alist[i] = []

    for (i,j) in e:
        Alist[i].append(j)
    return Alist




# For Undirected Graph

# Adjancey matrix using numpy
size = len(v)
Amatud = np.zeros((size,size), dtype = int)
for (i,j) in e:
    Amatud[i,j] = 1
    Amatud[i,j] = 1
# print(Amatud)

# Adjancey matrix using nested list
def creatematind(e,v):
    size = len(v)
    amatud = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        amatud.append(row)

    for (i,j) in e:
        amatud[i][j] = 1
        amatud[j][i] = 1
    return amatud

#adjancey list using dictionary.
def createlisind(e,v):
    size = len(v)
    alistud = {}
    for i in range(size):
        alistud[i] = []

    for (i,j) in e:
        alistud[i].append(j)
        alistud[j].append(i)
    return alistud


# Neighbours

def neighbours(graph , node):
    n = []
    col = len(graph[0])
    for i in range(col):
        if(graph[node][i]) == 1:
            n.append(i)
    return n


def weig_Dir_Mat(e,v):
    size = len(v)
    mat = np.zeros((size,size,2))
    for (i,j,w) in e:
        mat[i,j,0] = 1
        mat[i,j,1] = w
    return mat
    

def weig_Dir_lis(e,v):
    size = len(v)
    wlist = {}
    for i in range(size):
        wlist[i] = []
    for (i,j,d) in e:
        wlist[i].append((j,d))
    return wlist


def weig_unDir_Mat(e,v):
    size = len(v)
    mat = np.zeros((size,size,2) , dtype= int)
    for (i,j,w) in e:
        mat[i,j,0] = 1
        mat[i,j,1] = w
        mat[j,i,0] = 1
        mat[j,i,1] = w
    return mat
    

def weig_unDir_lis(e,v):
    size = len(v)
    wlist = {}
    for i in range(size):
        wlist[i] = []
    for (i,j,d) in e:
        wlist[i].append((j,d))
        wlist[j].append((i,d))
    return wlist


