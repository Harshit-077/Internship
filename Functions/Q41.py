# Find the 7th number in the Fibonacci sequence:
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))