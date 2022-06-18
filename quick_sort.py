def pivot(lis , lower , upper):
    pivot = upper
    a = lower-1
    b = lower
    while(b<upper):
        if(lis[b]<lis[pivot]):
            a+=1
            lis[a] , lis[b] = lis[b] , lis[a]
        b+=1
    lis[pivot] , lis[a+1] = lis[a+1] , lis[pivot]
    return a+1
    
    

def quick_sort(lis , l , r):
    if(l<r):
        p = pivot(lis, l , r)
        quick_sort(lis, l , p-1)
        quick_sort(lis, p+1 , r)

a = [5,4,1,3,2]
# print(a)
quick_sort(a , 0 , len(a)-1)
print(a)