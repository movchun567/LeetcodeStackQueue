from collections import deque

class FreqStack(object):

    def __init__(self):
        self.deque = deque()
        self.freq = deque()

    def freq_count(self, val):
        if val not in self.deque:
            self.freq.append(1)
        else:
            self.freq.append(self.deque.count(val) + 1)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq_count(val)
        self.deque.append(val)

    def pop(self):
        """
        :rtype: int
        """
        self.deque.reverse()
        self.freq.reverse()
        max_freq = max(self.freq)
        max_freq_index = list(self.freq).index(max_freq)
        data = self.deque[max_freq_index]
        del self.freq[max_freq_index]
        del self.deque[max_freq_index]
        self.deque.reverse()
        self.freq.reverse()
        return data

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()