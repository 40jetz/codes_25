class Stack:
    def __init__(self,size):
        self.stack = []
        self.size = size

    def push(self,element):
        if len(self.stack) == self.size:
            raise Exception("Stack is full")
        else:
            self.stack.append(element)
    def pop(self):
        if self.stack[-1] is None:
            print("Stack is empty")
        else:
            self.stack.pop()
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
    def __getitem__(self,index):
        return self.stack[index] 
    
    def __setitem__(self,index,value):
        self.stack[index] = value
if __name__ == "__main__":
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)


    print(stack)

    # stack.push(6)
    # print(stack) #Stack is full
    print(stack[-1])
    print(stack.peek())
