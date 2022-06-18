def inserction_sort(l):
    for i in range(len(l)):
        for j in range(i ,0, -1):
            if(l[j]<l[j-1]):
                l[j] , l[j-1] = l[j-1] , l[j]
            else:
                break

l = [5,4,1,3,2]
inserction_sort(l)
print(l)




