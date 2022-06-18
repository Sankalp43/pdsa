
class Maxheap:
    def __init__(self) -> None:
        self.a = []

    def max_heapify(self , k):
        l = (2*k) + 1
        r = (2*k) + 2
        largest = k

        if(l<len(self.a) and self.a[l] > self.a[largest]):
            largest = l

        if(r<len(self.a) and self.a[r] > self.a[largest]):
            largest = r
        
        if(largest != k):
            self.a[largest] , self.a[k] = self.a[k] , self.a[largest]
            self.max_heapify(largest)


    def build_max_heap(self , l):
        self.a = []
        for i in l:
            self.a.append(i)

        n = int((len(self.a)//2)-1)
        for k in range(n , -1 , -1):
            self.max_heapify(k)
    
    def delete_max(self):
        item = None
        if(self.a != []):
            self.a[0] , self.a[-1] = self.a[-1] , self.a[0]
            item = self.a.pop()
            self.max_heapify(0)
        return item

    def insert_in_maxheap(self , val):
        self.a.append(val)
        index = len(self.a) -1

        while(index>0):
            parent = (index-1)//2
            if(self.a[index]>self.a[parent]):
                self.a[index] , self.a[parent] = self.a[parent] , self.a[index]
                index = parent
            else:
                break


class Minheap:
    def __init__(self) -> None:
        self.a = []

    def min_heapify(self , k):
        l = (2*k) +1
        r = (2*k) + 2
        smallest = k

        if(l<len(self.a) and self.a[l] < self.a[smallest]):
            smallest = l
        
        if(r<len(self.a) and self.a[r] < self.a[smallest]):
            smallest = r

        if(k!= smallest):
            self.a[smallest] , self.a[k] = self.a[k] , self.a[smallest]
            self.min_heapify(smallest)

        
    def build_min_heap(self , l):
        self.a = []
        for i in l:
            self.a.append(i)

        n = (len(self.a)//2)-1
        for k in range(n , -1 , -1):
            self.min_heapify(k)

    def delete_min(self):
        item = None
        self.a[0] , self.a[-1] = self.a[-1] , self.a[0]
        if(self.a != []):
            item = self.a.pop()
            self.min_heapify(0)
        return item

    def insert_in_minheap(self , val):
        self.a.append(val)
        index = len(self.a) - 1
        while(index>0):
            parent = (index - 1)//2
            if(self.a[parent]>self.a[index]):
                self.a[parent] , self.a[index] = self.a[index] , self.a[parent]
                index = parent
            else:
                break

