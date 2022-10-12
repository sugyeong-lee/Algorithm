# def selection1(A, n) :
#     for i in range (0, n-1) :
#         m=i
#         for j in range(i+1, n) :
#             if A[j] < A[m] :
#                 m=j
#         A[i], A[m] = A[m], A[i]

def selection2(A, n) :
    for i in range (n-1, 0, -1) :
        m=i
        for j in range(i-1, -1, -1) :
            if A[j] > A[m] :
                m=j
        A[i], A[m] = A[m], A[i]