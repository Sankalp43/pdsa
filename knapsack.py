def MaxValue(items , w):
    m , n = len(items) , w
    
    c = []
    for i in range(m+1):
        row = []
        for j in range(n+1):
            row.append(0)
        c.append(row.copy())
    for i in range(1,m+1):
        for w in range(1 , n+1):
            if(items[i][0]>w):
                c[i][w] =c[i-1][w]
            else:
                c[i][w] = max(c[i-1][w] , items[i][1] + c[i-1][w-items[i][0]])
    return int(c[m][n])
            
        
w = 8
items = {1:(2,10), 2:(3,20), 3:(4,40)}

# ns = MaxValue(items , w)
# print(ns)

l = [1]*5
print(l)