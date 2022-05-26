import random, matplotlib.pylab as pylab

def runSim():
    bucket = [0,0,0,1,1,1]
    drawn = {'green':0, 'red':0}
    for i in range(6):
        draw = random.choice(bucket)
        bucket.remove(draw)
        if draw:
            drawn['red'] += 1
            drawn['green'] = 0
        else:
            drawn['green'] += 1
            drawn['red'] = 0
    return drawn['red'] == 3 or drawn['green'] == 3

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    numWins = 0
    for i in range(numTrials):
        if runSim():
            numWins += 1
    return numWins/numTrials

print(noReplacementSimulation(10000))