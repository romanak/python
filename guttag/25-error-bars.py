import random, matplotlib.pylab as pylab

def stdDev(X):
    """Assumes that (X) is a list of numbers
    Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)

def showErrorBars(minExp, maxExp, numTrials):
    """Assumes (minExp) and (maxExp) are positive integers; (minExp) < (maxExp)
    (numTrials) is a positive integer
    Plots mean fraction of heads with error bars"""
    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp+1):
        xVals.append(2**exp)
        fracHeads, mean, sd = flipSim(2**exp, numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.errorbar(xVals, means, yerr=2*pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean fraction of heads (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of heads with 95% confidence')
    pylab.show()

random.seed(0)
showErrorBars(3, 10, 100)