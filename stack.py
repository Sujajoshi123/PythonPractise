#Stack Data Structure in Python

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def get_stack(self):
        return self.items
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    

s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")

print (s.get_stack())

print (s.pop())
print (s.pop())

print (s.push("E"))
print (s.get_stack())

print (s.is_empty())

print (s.peek())



