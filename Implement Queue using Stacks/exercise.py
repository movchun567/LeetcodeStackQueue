class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return popped_data
    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data
    def is_empty(self):
        return self.size == 0


class MyQueue(object):

    def __init__(self):
        self.stack_en = Stack()
        self.stack_de = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_en.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack_de.is_empty():
            while not self.stack_en.is_empty():
                self.stack_de.push(self.stack_en.pop())
        return self.stack_de.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.stack_de.is_empty():
            while not self.stack_en.is_empty():
                self.stack_de.push(self.stack_en.pop())
        return self.stack_de.peek()
    
    def empty(self):
        """
        :rtype: bool
        """
        return self.stack_en.is_empty() and self.stack_de.is_empty()

    
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()