queue = []

# Enqueue operation
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueueing A, B, C:", queue)

# Peek operation
frontElement = queue[0] if queue else None
print("Front element after enqueueing:", frontElement)

# Dequeue operation
if queue:
    dequeuedElement = queue.pop(0)
else:
    dequeuedElement = None
print("Dequeued element:", dequeuedElement)
print("Queue after dequeueing:", queue)

# isEmpty operation
isEmpty = len(queue) == 0
print("Is queue empty?", isEmpty)

# Size operation
queueSize = len(queue)
print("Size of queue:", queueSize)