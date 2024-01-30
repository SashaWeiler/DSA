class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            
            elif operations[i] == 'D':
                stack.append(2*stack[-1])
            
            elif operations[i] == "C":
                stack.pop(-1)
            
            else:
                stack.append(int(operations[i]))
        return sum(stack)
        