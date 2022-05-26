def fib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    else:
        try:
            return memo[n]
        except KeyError:
            result = fib(n-1, memo) + fib(n-2, memo)
            memo[n] = result
            return result

for i in range(121):
    print('fib(' + str(i) + ') =', fib(i))