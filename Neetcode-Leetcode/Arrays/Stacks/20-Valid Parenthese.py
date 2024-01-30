def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        l = ["(", "{", "["]
        r = [")", "}", "]"]
        stack = []

        for value in s:
            if value in l:
                stack.append(value)
            elif value in r:
                if len(stack) == 0:
                    return False
                else:
                    if r.index(value) == l.index(stack.pop(-1)):
                        continue
                    return False
        if len(stack) == 0:
            return True
        return False

s = "()"
print(isValid(s))