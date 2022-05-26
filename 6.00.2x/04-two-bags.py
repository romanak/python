def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
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
                if (i>>j)%2 == 1:
                    subset.append(L[j])
            yield subset

    for bag1 in genPowerset(items):
        complimentarySet = []
        for item in items:
            if item not in bag1:
                complimentarySet.append(item)
        for bag2 in genPowerset(complimentarySet):
            yield (bag1, bag2)

for i in yieldAllCombos([1,2]):
    print(i)