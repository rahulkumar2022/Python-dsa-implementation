class queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue)==0
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    

#Create a queue object and test the methods
myQueue = queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)  
myQueue.enqueue(4)
print("Queue after enqueuing 4 elements:", myQueue.queue)
print("Dequeue element:", myQueue.dequeue())
print("Queue after dequeue:", myQueue.queue)
print("Peek element:", myQueue.peek())
print("Size of queue:", myQueue.size())
print("Is queue empty?", myQueue.is_empty())