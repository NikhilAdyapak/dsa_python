class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def traverse(self):
        for element in self.queue:
            print(element)

    def peek(self):
        return self.queue[-1]


# my_queue = Queue()
# for i in range(1,11):
#     my_queue.enqueue(i)

# print("size", my_queue.size())
# print("traverse")
# my_queue.traverse()
# print("peek")
# my_queue.peek()

# for i in range(20):
#     print(my_queue.dequeue())


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LLQueue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def queue_size(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.start = new_node
            self.end = new_node
        self.end.next = new_node
        self.end = new_node
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeue_node = self.start
        self.start = dequeue_node.next
        self.size -= 1
        return dequeue_node.data
    
    def traverse(self):
        if self.is_empty():
            return "Queue is empty"
        traverse_node = self.start
        while traverse_node != None:
            print(traverse_node.data)
            traverse_node = traverse_node.next
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.start.data
        
my_queue = LLQueue()

for i in range(1,11):
    my_queue.enqueue(i)

print("size", my_queue.queue_size())
print("traverse")
my_queue.traverse()

print("Dequeue")
for i in range(20):
    print(my_queue.dequeue())
