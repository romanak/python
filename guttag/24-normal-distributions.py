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

def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of ' + str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of heads')
    pylab.ylabel('Number of trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2, 'Mean = ' + str(round(mean, 4)) + '\nSD = ' + str(round(sd, 4)), size='x-large')

def makePlots(numFlips1, numFlips2, numTrials):
    pylab.figure()
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins = 20)
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)
    
    pylab.show()

random.seed(0)
makePlots(100, 1000, 100000)