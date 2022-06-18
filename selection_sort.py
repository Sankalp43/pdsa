def min(l , a , b):
    mi = a
    for i in range(a , b):
        if(l[i]<l[mi]):
            mi = i
    return mi


def selection_sort(l):
    for i in range(len(l)):
        mi = min(l,i , len(l))
        l[i] , l[mi] = l[mi] , l[i]

        
a = [5,4,1,3,2]
selection_sort(a)
print(a)
     













