def QuickSort(A, start, end):
    if(start < end):
        pIndexes = Partition(A, start, end)
        QuickSort(A, start, pIndexes[0]-1)
        QuickSort(A, pIndexes[0]+1, pIndexes[1]-1)
        QuickSort(A, pIndexes[1]+1, end)

def Partition(A, start, end):
    if A[start] > A[end]:
        A[start], A[end] = A[end], A[start]
    pivot1 = A[start]
    pivot2 = A[end]
    p1Index = start+1
    p2Index = end-1
    i = start+1
    while i <= p2Index:

        # Smaller than the first pivot
        if A[i] < pivot1:
            A[i], A[p1Index] = A[p1Index], A[i]
            p1Index += 1

        # Greater or equal to the second pivot
        elif A[i] >= pivot2:
            # While p2Index is greater than i and  points to a number bigger than the second pivot move it forwards
            while A[p2Index] > pivot2 and i < p2Index:
                p2Index -= 1
            # Swap item with p2Index and move p2Index forwards
            A[i], A[p2Index], = A[p2Index], A[i]
            p2Index -= 1
            # A[i] is a different value now as it has been swapped, check if it is bigger than the first pivot
            if A[i] < pivot1:
                A[i], A[p1Index] = A[p1Index], A[i]
                p1Index += 1
        i += 1
    A[start], A[p1Index-1] = A[p1Index-1],A[start]
    A[end], A[p2Index+1] = A[p2Index+1], A[end]

    return [p1Index-1, p2Index+1]

t = [5,12,2,6,1,10,3,7,8,13,9,11]
QuickSort(t,0,len(t)-1)
print(t)