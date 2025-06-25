class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print("Stack after pushing 1, 2, 3:", myStack.stack)


print("Top element after pushing:", myStack.peek())

print("Popped element:", myStack.pop())
print("Stack after popping:", myStack.stack)
print("Is this stack empty? ",myStack.isEmpty())
print("Size of stack: ",myStack.size())