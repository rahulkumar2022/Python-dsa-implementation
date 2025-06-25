class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def traverse_and_print(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
traverse_and_print(node1)