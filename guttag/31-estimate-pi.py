import random
#random.seed(0)
def stdDev(X):
    """Assumes that (X) is a list of numbers
    Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def CV(X):
    mean = sum(X)/len(X)
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

def rollDie():
    return random.choice([1,2,3,4,5,6])

def throwNeedles(numNeedles):
    inCircle = 0
    for n in range(numNeedles):
        x = random.random()
        y = random.random()
        if (x*x+y*y)**0.5 <= 1.0:
            inCircle += 1
    # counting needles in one quadrant only, so multiply by 4
    return 4*inCircle/numNeedles

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. = ' + str(round(curEst, 5)) + ', Std. Dev. = ' + str(round(sDev, 5)) +\
        ', Needles = ' + str(numNeedles))
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2.0:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

estPi(0.01, 100)