import random, matplotlib.pylab as pylab

def stdDev(X):
    """Assumes that (X) is a list of numbers
    Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def plotData(x, y, title, xlabel, ylabel, style, logX=False, logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()
    pylab.plot(x, y, style)

def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)

def CV(X):
    mean = sum(X)/len(X)
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

def flipPlot2(minExp, maxExp, numTrials):
    """Assumes (minExp) and (maxExp) are positive integers; (minExp) < (maxExp)
    (numTrials) is a positive integer
    Plots summaries of results of (numTrials) trials of
    2**(minExp) to 2**(maxExp) coin flips"""
    ratioMeans, diffsMeans, ratiosSDs, diffsSDs, xAxis = [], [], [], [], []
    ratiosCVs, diffsCVs = [], []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        ratioMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString = ' (' + str(numTrials) + ' Trials)'
    
    title = 'Mean heads / tails ratios' + numTrialsString
    plotData(xAxis, ratioMeans, title, 'Number of flips',
        'Mean heads / tails', 'bo', True)
    
    title = 'SD heads / tails ratios' + numTrialsString
    plotData(xAxis, ratiosSDs, title, 'Number of flips',
        'Standard deviation', 'ro', True, True)

    title = 'Mean |heads - tails|' + numTrialsString
    plotData(xAxis, diffsMeans, title, 'Number of flips',
        'Mean |heads - tails|', 'bo', True, True)

    title = 'SD |heads - tails|' + numTrialsString
    plotData(xAxis, diffsSDs, title, 'Number of flips',
        'Standard deviation', 'ro', True, True)

    title = 'Coefficient of variation |heads - tails|' + numTrialsString
    plotData(xAxis, diffsCVs, title, 'Number of flips',
        'Coefficient of variation', 'bo', True)

    title = 'Coefficient of variation heads / tails ratios' + numTrialsString
    plotData(xAxis, ratiosCVs, title, 'Number of flips',
        'Coefficient of variation', 'ro', True, True)

    pylab.show()

random.seed(0)
flipPlot2(4, 20, 20)