import heapq

A=[]
A =list(map(int, input().split()))

i = 0
m=[]
while i <= len(A)-1:
	m.append(A[i])
	k = i//3+1
	print(m)