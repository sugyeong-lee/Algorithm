def insertion_Sort(A, n):
    for i in range(1, n):
        j = i-1
        while j >= 0 and A[j]>A[j+1]:
            A[j],A[j+1] = A[j+1], A[j]
            j = j-1