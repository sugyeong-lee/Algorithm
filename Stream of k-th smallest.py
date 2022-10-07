import heapq

A=[]
A =list(map(int, input().split()))  # 리스트 입력

def quick(A, k):    # Quick Selsction 구현
	p = A[len(A)//5]  # heap 자료구조의 규칙성을 이용하여 피봇을 정하려 했지만 실패하여 가장 시간복잡도가 작았던 len(A)//5를 피봇으로 정함
	S, L, M =[], [], []
	heapq.heapify(A)   # heap 자료구조 사용(모듈 이용)
	
	for i in range(len(A)):  # 피봇 값을 비교하여 L,S,M으로 배열 분할
		if A[i] < p: 
			S.append(A[i])
		elif A[i] > p: 
			L.append(A[i])
		else: 
			M.append(A[i])
	
	if len(S) >= k:        # 재귀과 함께 분할한 배열을 기준으로 k번째 값을 찾고 return
		return quick(S,k)
	elif len(S) + len(M) < k:
		return quick(L,k-len(S)-len(M))
	else:
		return p
	
i, s = 0, 0
m=[]
while i <= len(A)-1:  # 차례로 배열과 k번째 값 함수 입력
	m.append(A[i])
	k = i//3+1
	s += quick(m, k)
	i	+= 1
	
print(s)

# 사용한 자료구조 : 힙 자료구조 (최소 힙) : 완전이진트리 형태로 우선순위 큐를 위해 만들어진 자료구조이다. 여러 개의 값 중 최댓값, 최솟값을 빠르게 찾아낼 수 있다. 각 노드의 key값이 그 자식노드의 key값보다 크지 않다. 키 값의 대소관계는 부모와 자식 노드 사이에만 성립한다. 또한 i번째 노드의 왼쪽 자식은 2i, 오른쪽 자식 노드는 2i+1, 부모 노드는 i/2로 성립된다.

# 사용한 알고리즘 : Quick_Select : 여러 값이 주어졌을 때 k번쨰로 작은 값이나 큰 값을 찾을 때 좋은 알고리즘이다. 피봇 값을 기준으로 배열을 분할한다. (피봇보다 작은 값은 S집합에 큰 값은 L집합에 그리고 같은 값은 M에 할당하는 방식이다.) 그리고 재귀적으로 범위를 줄여나가면서 각 집합의 원소의 수롤 기준으로 k와 비교하여 k번째 값을 찾아낸다.

# 수행시간
# 1. quick(A, k) 함수 안
# heapify() 함수 : O(n) : 리스트 내부 원소들이 힙 구조에 맞게 재배치(최소값이 인덱스 0으로)
# for문+if문 : O(nlogn) : len(A)-1 반복 및 조건에 따라 append() 연산 -> 최악의 경우 O(n^2) : T(n/2)+cn
# append() 함수 : O(n) : 리스트 맨뒤에 원소 추가
# 2. quick(A, k) 함수 밖
# while문 : O(logn) : len(A)-1번 반복
# append() 함수 : O(n) : 리스트 맨뒤에 원소 추가
# -> 결과적으로 : 최악의 경우 : O(n^2), 평균 : O(n)
# 3. 실제 수행시간
# 0.03->0.02->0.07->0.14->0.36->7.35 로 약 2배씩 증가하는 것 같으나 0->7의 증가로 규칙을 파악하기 어려움
# 따라서 0->7의 증가에서 최악의 경우를 만난 것으로 간주 : O(n^2)
