class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def is_empty(self):
        return self.size == 0
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.head
        self.head = popped_node.next
        self.size -= 1
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.data
    
    def stack_size(self):
        return self.size
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print()

my_stack = Stack()
# for i in range(1,11):
#     my_stack.push(i)

# # my_stack.peek()

# # my_stack.traverse()

# for i in range(20):
#     print(my_stack.pop())
    
