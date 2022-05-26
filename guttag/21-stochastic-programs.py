import random, matplotlib.pylab as pylab
 
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])
 
def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

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
    print(mean)

def flipPlot(minExp, maxExp): 
    """Assumes (minExp) and (maxExp) are positive integers; (minExp) < (maxExp)
    Plots results of 2**(minExp) to 2**(maxExp) coin flips"""
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/numTails)
        diffs.append(abs(numHeads - numTails))
    pylab.figure()
    pylab.title('Difference between heads and tails')
    pylab.xlabel('Number of flips')
    pylab.ylabel('|heads - tails|')
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(xAxis, diffs, 'ro')

    pylab.figure()
    pylab.title('Heads/tails ratios')
    pylab.xlabel('Number of flips')
    pylab.ylabel('heads/tails')
    pylab.semilogx()
    pylab.plot(xAxis, ratios, 'bo')
    pylab.show()

testRoll()
flipSim(100,100)
random.seed(0)
flipPlot(4, 20)