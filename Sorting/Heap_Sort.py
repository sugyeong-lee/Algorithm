def make_heap(A) :
    n = len(A)
    for k in range(n-1, -1, -1):
        heapify_down(A, k, n)
        
def heapify_down(self, k, n):
    while 2*k+1 < n:
        L, R = 2*k+1, 2*k+2
        if L < n and self.A[L] > self.A[k] :
            m = L
        else :
            m=k
        if R<n and self.A[R] > self.A[m] :
            m=R
        if m!=k :
            self.A[k], self.A[m] = self.A[m], self.A[k]
            k=m
        else: break

def heap_sort(A) :
    n = len(A)
    for k in range(len(A)-1, -1, -1):
        A[0], A[k] = A[k], A[0]
        n = n-1
        heapify_down(A, 0, n)

A=list(map(int, input().split()))
B=heap_sort(A)
print(B)