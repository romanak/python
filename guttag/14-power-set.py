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
            # i//(2**j) is equivalent to >> bitwise operator
            if (i//(2**j))%2 == 1:
                subset.append(L[j])
        powerset.append(subset)
    return powerset

def genAlphabet(n):
    """
    Assumes (n) is a non-negative integer less than 27
    Returns a list of size (n) of letters in alphabetical order
    """
    assert (n >= 0) and (n <= 26), 'n must be in the interval [0,26]'
    result = []
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(n):
        result.append(a[i])
    return result

def testPowerset(n):
    for i in range(n):
        testset = genAlphabet(i)
        print('List size:', len(testset))
        powerset = genPowerset(testset)
        print('Powerset size:', len(powerset))

testPowerset(20)