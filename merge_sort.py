def merge(lis , l , mid , r):
    n1 = mid-l+1
    n2 = r-mid
    a1 = []
    for i in range(n1):
        a1.append(lis[i+l])
    
    a2 = []
    for i in range(n2):
        a2.append(lis[mid+i+1])

    a = 0
    b = 0
    c = l

    while(a<n1 and b<n2):
        if(a1[a]<=a2[b]):
            lis[c] = a1[a]
            a+=1
            c+=1
        else:
            lis[c] = a2[b]
            b+=1
            c+=1


    while(a<n1):
        lis[c] = a1[a]
        c+=1
        a+=1
    while(b<n2):
        lis[c] = a2[b]
        b+=1
        c+=1
    



def merge_sort(lis,l,r):
    if(l<r):
        mid = (l+r)//2
        merge_sort(lis , l , mid)
        merge_sort(lis , mid+1 , r)
        merge(lis , l , mid , r)


t = [5,4,2,3,1]
merge_sort(t , 0 , len(t)-1)
print(t)