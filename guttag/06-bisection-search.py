x = 0.25
epsilon = 0.01
numGuesses = 0
low = min(-1.0, x)
high = max(1.0, x)
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)