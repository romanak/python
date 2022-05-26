count = 0
def fib(n):
    global count
    if n == 2:
        count += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5), count)