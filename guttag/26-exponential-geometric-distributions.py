import random, matplotlib.pylab as pylab

def clear(n, p, steps):
    """Assume (n), (steps) are positive integers, (p) is a float
    (n): initial number of molecules
    (p): the probability of a molecule being cleared
    (steps): the length of the simulation"""
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    
    pylab.figure()
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules remaining')
    pylab.title('Clearance of drug')
    pylab.semilogy()
    pylab.show()

def successfulStarts(eventProb, numTrials):
    """Assumes (eventProb) is a float representing a probability
    of a single attempt being successful. (numTrials) is a positive
    integer. Returns a list of the number of attempts needed before
    a success for each trial."""
    triesBeforeSuccess = []
    for t in range(numTrials):
        consecFailures = 0
        while random.random() > eventProb:
            consecFailures += 1
        triesBeforeSuccess.append(consecFailures)
    
    pylab.figure()
    pylab.hist(triesBeforeSuccess, bins=14)
    pylab.xlabel('Tries before success')
    pylab.ylabel('Number of occurrences out of ' + str(numTrials))
    pylab.title('Probability of starting each try ' + str(eventProb))
    pylab.show()

#clear(1000, 0.01, 1000)
successfulStarts(0.5, 5000)