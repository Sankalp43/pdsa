class Tree():
    def __init__(self, val = None) -> None:
        self.value = val
        if(self.value):
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def isEmpty(self):
        return self.value == None

    def isLeaf(self):
        return (self.value != None and self.left.isEmpty() and self.right.isEmpty())

    def inorder(self):
        if(self.isEmpty()):
            return []
        return self.left.inorder() + [self.value] + self.right.inorder()
    
    def __str__(self) -> str:
        return(str(self.inorder()))

    def find(self , v):
        if(self.isEmpty()):
            return False
        if(self.value == v):
            return True
        if(self.value <v):
            return self.right.find(v)
        if(self.value>v):
            return self.left.find(v)

    def minval(self):
        if(self.left.isEmpty()):
            return self.value
        return self.left.minval()

    def maxval(self):
        if(self.right.isEmpty()):
            return self.value
        return self.right.maxval()

    def insert(self , v):
        if(self.isEmpty()):
            self.value = v
            self.left = Tree()
            self.right = Tree()
        
        if(self.value == v):
            return
        
        if(self.value<v):
            self.right.insert(v)
            return

        if(self.value >v):
            self.left.insert(v)
            return


    def delete(self , v):
        if(self.isEmpty()):
            return
        if(self.value<v):
            return self.right.delete(v)
        if(self.value>v):
            return self.left.delete(v)
        if(self.value == v):
            if(self.isLeaf()):
                self.makeEmpty()
                return
            elif(self.left.isEmpty()):
                self.copyright()
                return
            elif(self.right.isEmpty()):
                self.copyleft()
                return

            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return

            
            
    def makeEmpty(self):
        self.value = None
        self.left = None
        self.right = None
    
    def copyright(self):
        self.value = self.right.value
        self.right = self.right.right
        self.left = self.right.left

    def copyleft(self):
        self.value = self.left.value
        self.right = self.left.right
        self.left = self.left.left


        

