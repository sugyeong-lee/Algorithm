def quick1(A) :
    if len(A) <=1 :
        return A
    p = A[0]
    S, M, L = [], [], []
    for x in A :
        if x<p :
            S.append(x)
        elif x==p :
            M.append(x)
        else :
            L.append(x)
    return quick1(S) + M + quick1(L)

# def quick2(A,first, last) :
#     if first >= last :
#         return
#     left, right = first+1, last
#     p = A[first]
#     while left <= right :
#         while left <= last and A[left] < p :
#             left = left+1
#         while right > first and A[right] >= p :
#             right = right-1
#         if left <= right :
#             A[left], A[right] = A[right], A[left]
#             left = left+1
#             right = right-1
#     A[first], A[right] = A[right], A[first]
    quick2(A, first, right-1)
    quick2(A, right, last)
