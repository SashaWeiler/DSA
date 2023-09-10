def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    stack = []
    l1 = 0
    total_sum = 0
    
    for i in range(len(operations)):
        
        if (operations[i] == '+'):
            new_sum = stack[l1] + stack[l1 -1]
            stack.append(new_sum)
            total_sum += new_sum
            l1 += 1
        
        elif (operations[i] == 'D'):
            stack.append(2*stack[l1])
            total_sum += 2*stack[l1]
            l1 += 1
        
        elif(operations[i] == 'C'):
            total_sum -= stack.pop(-1)
            l1 -= 1
        
        else:

            stack.append(int(operations[i]))
            total_sum += int(operations[i])

    return total_sum

arr = ["5","2","C","D","+"]

total = calPoints(arr)
print(total)