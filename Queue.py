class Queue:
    def __init__(self) -> None:
        self.l = []
    
    def add(self , value):
        self.l.append(value)
    
    def remove(self):
        a = self.l.pop(0)   # FIFO
        return a

    def isEmpty(self):
        return self.l == []
    
