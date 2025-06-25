class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,item):
        new_node = Node(item)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.isEmpty():
            return "Satck is Empty"
        return self.head.data
    
    def isEmpty(self):
        return self.size == 0
    
    def size(self):
        return self.size
    
    def traverse_and_print(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
print("Stack after pushing A, B, C:", myStack.head.data);
myStack.traverse_and_print()


