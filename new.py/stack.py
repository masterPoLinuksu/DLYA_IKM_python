from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size_stack = 0

    def push(self, color, count=1):
        node = Node(color, count)
        node.next = self.top
        self.top = node
        self.size_stack += 1

    def pop(self):
        if self.top is None:
            raise IndexError("pop из пустого стека")
        node = self.top
        self.top = node.next
        self.size_stack -= 1
        return node.color, node.count

    def peek(self):
        if self.top is None:
            raise IndexError("peek в пустом стеке")
        return self.top.color, self.top.count

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size_stack
