class MinStack(object):

    def __init__(self):
        self.data = []
        self.minstack = []
        # Must be named topValue due to the fact that that one of the 
        # class methods is called top

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.data.append(val)

        if len(self.data) == 1:
            self.minstack.append(val)

        if val < self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])


    def pop(self):
        """
        :rtype: None
        """
        self.data.pop(-1)
        self.minstack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
obj.top()
print(obj.getMin())
