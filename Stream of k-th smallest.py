s = 0
A=[]
A =list(map(int, input().split()))
	
def quick_select(A, k):   
	p = A[0]
	S, L, M =[], [], []
	
	for i in range(len(A)):
		if A[i] < p: 
			S.append(A[i])
		elif A[i] > p: 
			L.append(A[i])
		else: 
			M.append(A[i])
			
	if len(S) >= k:
		return quick_select(S,k)
	elif len(S) + len(M) < k:
		return quick_select(L,k-len(S)-len(M))
	else:
		return p
	
for i in range(len(A)):
	k = i//3+1
	a = quick_select(A, k)
	s += a
	
print(s)