def merge_sort(A, first, last): # merge sort A[first] ~ A[last]
    if first >= last:
        return

    m = (first+last)//2
    merge_sort(A, first, m)
    merge_sort(A, m+1, last)

    B = []
    i, j = first, m+1
    while i <= m and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    for i in range(i, m+1):
        B.append(A[i])
    for j in range(j, last+1):
        B.append(A[j])
    for k in range(first, last+1):
        A[k] = B[k-first]

