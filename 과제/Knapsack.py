# 분할 가능, 물건 나눠 담기
def fractional_knapsack(n_item, size, profit, knapsack):
	# n_item : n개의 아이템
	# size[] : 크기
	# profit[] : 가치
	# knapsack : 배낭

	if knapsack <= 0: return 0       # 빈 공간이 없거나 0 보다 작으면 return 0

	size_sum = 0                     # size_sum : 현재까지 선택한 아이템의 크기 합
	profit_sum = 0                   # profit_sum : 현재까지 선택한 아이템의 가치 합

	for i in range(n_item):
		if size_sum + size[i] <= knapsack: # 배낭에 쏙 들어가면 전체 선택
			profit_sum += profit[i]
			size_sum += size[i]
		else:                              # 넘치면 잘라서 선택
			profit_sum += (knapsack-size_sum) * (profit[i]/size[i])
			size_sum = knapsack
			break
	return profit_sum

# 0/1 knapsack
def Knapsack(i, knapsack_T): # x[i] = 1인 경우와 0인 경우를 각각 시도함
	# knapsack_T : 배낭의 남은 공간

	x = []
	if i >= n_item or knapsack_T <= 0:
		print(x)
		return     # 바닥조건
	
	size_sum, profit_sum, MaxProfit = 0, 0, 0 # 현재 상태에서 선택된 크기 합, 가치 합, 최대 이익
	
	# 아이템 i를 선택하여 배낭에 넣는 경우: x[i] = 1 이라면?
	# i+1 이후 아이템에 대해, 남은 배낭공간(T-size[i])에 fractional로 채울 수 있는 최대 가치 계산
	if x[i] == 1:
		if size_sum+size[i] <= knapsack: # 계속 탐색해야 한다면
			B = fractional_knapsack(n_item-(i+1), size[n_item+1:], profit[n_item+1:], size-size[n_item])
			if profit_sum+profit[n_item] > MaxProfit: # 계속 탐색해야 한다면
				MaxProfit # 업데이트 + x를 solution으로 카피(기록)	
				Knapsack(n_item+1, K_size[i])
	
	# 아이템 i를 선택하지 않는 경우: x[i] = 0 이라면?
	if x[i] == 0:
		B = fractional_knapsack(n_item-(i+1), size[i+1:], profit[i+1:], T)
		if (p + B) > MaxProfit: # 계속 탐색해야 한다면
			Knapsack(n_item+1, size)

# n, size, profit, K 입력으로 주어짐
# x = [0, 0, ..., 0] # 아이템 i가 선택되면 x[i] = 1, 아니면 x[i] = 0이 됨
# MaxProfit = 현재까지 가장 큰 가치 값 [전역변수]
# solution = [] [전역변수]
# Knapsack(0, K) # [주의] 아이템의 번호가 0부터 시작한다고 가정

knapsack = int(input())
n_item = int(input())
size = list(map(int, input().split()))
profit = list(map(int, input().split()))