class Stack:
    def __init__(self) -> None:
        self.l = []

    def add(self , val):
        self.l.append(val)
    
    def remove(self):
        a = self.l.pop()
        return a

    def is_Empty(self):
        return self.l == []

