class Node:
    def __init__(self, value = None) -> None:
        self.val = value
        self.next = None
    
    def is_empty(self):
        return self.val == None

    def append(self , value):
        if self.is_empty():
            self.val = value
        else:
            a = self
            while(a.next!= None):
                a = a.next
            node = Node(value)
            a.next = node
        

    def display(self):
        temp = self
        while(temp.next!= None):
            print(temp.val)
            temp = temp.next
        print(temp.val)


    def delete(self, x):
        if(self.is_empty()):
            return
        if(self.next == None):
            if(self.val == x):
                self.val = None
            return
    
        temp = self
        while(temp.next.next!= None):
            if(temp.val == x):
                temp.val = temp.next.val
                temp.next = temp.next.next
                return
        if(temp.val == x):
            temp.val = temp.next.val
            temp.next = temp.next.next
            return
        if(temp.next.val ==x):
            temp.next = temp.next.next
            
        


            

        





