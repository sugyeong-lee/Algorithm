def bubble(A, n) :
    for i in range (n) :
        for j in range (n-1, i, -1):
            if A[j-1] > A[j] :
                A[j-1], A[j] = A[j], A[j-1]