def genPowerset(L):
    """Returns powerset of size 0 - len(L) for (L)"""
    if len(L) == 0:
        # If the list is empty, return the empty list
        return [[]]
    powerset = []
    first_elt = L[0]
    rest_list = L[1:]
    # Strategy: Get powerset of rest_list; for each
    # of those subsets, a full powerset list will contain both
    # the original powerset as well as a version of the powerset
    # that contains first_elt
    for partial_subset in genPowerset(rest_list):
        powerset.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        powerset.append(next_subset)
    return powerset

print(genPowerset([1,2,3]))