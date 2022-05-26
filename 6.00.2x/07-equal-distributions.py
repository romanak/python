import random, matplotlib.pylab as pylab

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1

def testDist(trials):
    x, d1, d2 = [], [], []
    for n in range(trials):
        x.append(n)
        d1.append(dist1())
        d2.append(dist2())
    pylab.figure()
    pylab.title('Distribution')
    pylab.plot(x, d1, 'ro', label='Dist1')
    pylab.plot(x, d2, 'bo', label='Dist2')
    pylab.xlabel('Number of trials')
    pylab.ylabel('Random float')
    pylab.legend(loc = 'upper right')
    pylab.show()
testDist(100)