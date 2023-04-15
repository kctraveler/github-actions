from collections import deque

class Stack:
    
    def __init__(self, data=None) -> None:
        if data == None:
            self.stack = deque()
        elif isinstance(data, list):
            self.stack = deque(data)
        else:
            raise TypeError("data must be of type list")
        
    def add(self, item) -> None:
        self.stack.append(item)
        
    def pop(self) -> object:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise IndexError
        
    def peek(self) -> object:
        if (len(self.stack) > 0):
            next = self.pop()
            self.add(next)
            return next
        else:
            raise IndexError
    
    def isEmpty(self) -> bool:
        return bool(len(self.stack) == 0)
    
    def __str__(self) -> str:
        string = str(self.stack)[5:]
        return "Stack" + string
    
    def __len__(self) -> int:
        return len(self.stack)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.stack)>0:
            return self.pop()
        else:
            raise StopIteration
    
    
        
    
if __name__ == "__main__": # pragma: no cover
    stack = Stack()

    for i in range(10):
        stack.add(i)
    
    print(f"Length: {len(stack)}")
    print(f'Peek {stack.peek()}') 
    print(f'Length: {len(stack)}') 
    print(f'Pop: {stack.pop()}') 
    print(f'Peek: {stack.peek()}')
    print(f'Length: {len(stack)}')

    for object in stack:
        print(object)
        
    print(f'Length: {len(stack)}')
    
        