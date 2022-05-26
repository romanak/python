import random
class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def density(self):
        return self.getValue()/self.getWeight()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.weight) + '>'

def buildItems(names, values, weights):
    items = []
    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))
    return items

def greedy(items, maxWeight, keyFunction):
    """Assumes (items) a list, (maxWeight) >= 0,
         keyFunction maps elements of (items) to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalWeight = 0, 0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(items, maxWeight):
    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, Item.getValue)
    print('\nUse greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, lambda x: 1/Item.getWeight(x))
    print('\nUse greedy by density to to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, Item.density)

def genPowerset(L):
    """
    Assumes (L) is a list
    Returns a list of lists that contains all possible combinations of the elements of (L).
    For example, if (L) is [1, 2], it will return [[], [1], [2], [1,2]]
    """
    n = len(L)
    powerset = []
    # power set will have 2^(n) items; iterate over each item to fill in values
    for i in range(2**n):
        subset = []
        for j in range(n):
            # use a vector of binary representation of (i) to fill in corresponding values from (L)
            if (i//(2**j))%2 == 1:
                subset.append(L[j])
        powerset.append(subset)
    return powerset

def bruteForce(powerset, maxWeight):
    bestVal, bestSet = 0, None
    for items in powerset:
        itemsVal, itemsWeight = 0, 0
        for item in items:
            itemsVal += item.getValue()
            itemsWeight += item.getWeight()
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestVal, bestSet)

def testBruteForce(items, maxWeight, printItems = True):
    powerset = genPowerset(items)
    print('\nUse brute force to to fill knapsack of size', maxWeight)
    val, taken = bruteForce(powerset, maxWeight)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

def searchTree(toConsider, avail):
    """Assumes (toConsider) a list of items, (avail) a weight
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the items of that solution"""
    global callsCount
    callsCount += 1
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        # Explore right branch only
        result = searchTree(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = searchTree(toConsider[1:], avail - nextItem.getWeight())
        # Add current item
        withVal += nextItem.getValue()
        withToTake = withToTake + (nextItem,)
        # Explore right branch
        withoutVal, withoutToTake = searchTree(toConsider[1:], avail)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake)
        else:
            result = (withoutVal, withoutToTake)
    return result

def fastSearchTree(toConsider, avail, memo={}):
    """Assumes (toConsider) a list of items, (avail) a weight
    (memo) is used only by recursive calls
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the items of that solution"""
    # len(toConsider) is a compact way of representing the items still to be considered
    # THis works because items are always removed from the same end (the front)
    # of the list toConsider
    global callsCount
    callsCount += 1
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        # Explore right branch only
        result = fastSearchTree(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = fastSearchTree(toConsider[1:], avail - nextItem.getWeight(), memo)
        # Add current item
        withVal += nextItem.getValue()
        withToTake = withToTake + (nextItem,)
        # Explore right branch
        withoutVal, withoutToTake = fastSearchTree(toConsider[1:], avail, memo)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake)
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testSearchTree(items, maxWeight, printItems = True):
    print('\nUse search tree to to fill knapsack of size', maxWeight)
    val, taken = searchTree(items, maxWeight)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

def testFastSearchTree(items, maxWeight, printItems = True):
    print('\nUse fast search tree to to fill knapsack of size', maxWeight)
    val, taken = fastSearchTree(items, maxWeight)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

def buildManyItems(numItems, maxVal, maxWeight):
    items = []
    for i in range(numItems):
        items.append(Item(str(i), random.randint(1, maxVal), random.randint(1, maxWeight)*random.random()))
    return items

def bigTest(numItems, maxWeight):
    global callsCount
    items = buildManyItems(numItems, 20, 20)
    testGreedys(items, maxWeight)
    callsCount = 0
    testFastSearchTree(items, maxWeight)
    print('Number of items:', numItems, 'Power set size:', 2**numItems, 'Number of calls:', callsCount)
    # callsCount = 0
    # testSearchTree(items, maxWeight)
    # print('Number of items:', numItems, 'Power set size:', 2**numItems, 'Number of calls:', callsCount)

# names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
# values = [175,90,20,50,10,200]
# weights = [10,9,4,2,1,20]
# items = buildItems(names, values, weights)
# testGreedys(items, 20)
# testBruteForce(items, 20)
# testSearchTree(items, 20)

bigTest(16, 40)