def exponent(x, n):
    if n != 0:
        return x * exponent(x, n-1)
    else:
        return 1
    
a = exponent(3, 4)
print(a)