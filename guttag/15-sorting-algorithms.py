def selectionSort(L):
    """Assumes that (L) is a list of integers
    Sorts the list (L) in ascending order"""
    for i in range(len(L)-1):
        minIndx = i
        for j in range(i+1, len(L)):
            if L[j] < L[minIndx]:
                minIndx = j
        if minIndx != i:
            L[i], L[minIndx] = L[minIndx], L[i]

def bubbleSort(L):
    """Assumes that (L) is a list of integers
    Sorts the list (L) in ascending order"""
    clear = False
    while not clear:
        clear = True
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                clear = False
                L[i], L[i+1] = L[i+1], L[i]

def swapSort(L): 
    """Assumes that (L) is a list of integers
    Sorts the list (L) in ascending order"""
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]

def mergeSort(L):
    """Assumes that (L) is a list of integers
    Sorts the list (L) in ascending order"""
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left, right)

l = [2,7,4,9,0,3]
#selectionSort(l)
#bubbleSort(l)
#swapSort(l)
l = mergeSort(l)
print(l)