epsilon = 0.01
k = 19888394389123
guess = k/2
numGuesses = 0
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuesses += 1
    if numGuesses%1000000 == 0:
        print('numGuesses =', numGuesses, 'guess =', guess)
print('numGuesses =', numGuesses)
print('Square root of', k, 'is about', guess)