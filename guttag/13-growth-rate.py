def f(x):
    ans = 0
    for i in range(1000):
        ans += 1
    print('Constant growth:', ans)

    for i in range(x):
        ans += 1
    print('Linear growth:', ans)

    for i in range(x):
        for j in range(x):
            ans += 1
    print('Quadratic growth:', ans)

    return ans

f(10000)