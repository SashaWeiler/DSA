def bad_fib(n):
    if n <= 1:
        return (n,0)
    else:
         return fib(n-1) + fib(n-2)

def fib(n):
    if n <= 1:
        return (n,0)
    else:
         a, b = fib(n-1)
         return (a+b, a)