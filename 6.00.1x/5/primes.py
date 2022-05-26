def genPrimes():
    primes = []
    n = 2
    while True:
        prime = True
        for i in primes:
            if n%i == 0:
                prime = False
                break
        if prime:
            primes.append(n)
            yield n
        n += 1

p = genPrimes()
#for i in range(10):
#    print(p.__next__())

def g():
    n = 0
    while True:
        yield n
        n += 1

a = g()
for i in range(10):
    print(a.__next__())