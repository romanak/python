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
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
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

def searchTree(powerset, maxWeight):
    bestVal, bestSet = 0.0, None
    for items in powerset:
        itemsVal, itemsWeight = 0.0, 0.0
        for item in items:
            itemsVal += item.getValue()
            itemsWeight += item.getWeight()
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestVal, bestSet)

def testSearchTree(items, maxWeight, printItems = True):
    powerset = genPowerset(items)
    print('\nUse search tree to to fill knapsack of size', maxWeight)
    val, taken = searchTree(powerset, maxWeight)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
values = [175,90,20,50,10,200]
weights = [10,9,4,2,1,20]
items = buildItems(names, values, weights)

testGreedys(items, 20)
testSearchTree(items, 20)