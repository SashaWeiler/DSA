class MinStack(object):

    def __init__(self):
        self.data = []
        self.min = 0
        # Must be named topValue due to the fact that that one of the 
        # class methods is called top
        self.topValue = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.data.append(val)
        self.topValue = val

        if len(self.data) == 1:
            self.min = val

        if val < self.min:
            self.min = val

    def pop(self):
        """
        :rtype: None
        """
        popped = self.data.pop(-1)
        # Edgecase not considered where after popping there may be nothing
        # Can't check value of index if there isn't anything there
        if not len(self.data) == 0:
            self.topValue = self.data[-1]
            if popped == self.min:
                # Not actually O(1)
                self.min = min(self.data)
        

    def top(self):
        """
        :rtype: int
        """
        return self.topValue
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
obj.top()
print(obj.getMin())
