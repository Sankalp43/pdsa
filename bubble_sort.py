def bubble_sort(l):
    for i in range(len(l)):
        for j in range(1 , len(l)-i):
            if(l[j] < l[j-1]):
                l[j] , l[j-1] = l[j-1] , l[j]
    
l = [5,4,2,1,3]
bubble_sort(l)
print(l)


