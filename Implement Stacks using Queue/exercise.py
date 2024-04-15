class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def push(self, data):
        new = Node(data)
        if not self.front:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        self.size += 1
    
    def pop(self):
        if not self.front:
            return None
        data = self.front.data
        if self.front == self.rear:
            self.rear = None
        self.front = self.front.next
        self.size -= 1
        return data
    
    def is_empty(self):
        return self.front is None
    


class MyStack(object):

    def __init__(self):
        self.queue = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.push(x)
        for _ in range(self.queue.size - 1):
            self.queue.push(self.queue.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.queue.front.data

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()