def find_way_from_maze(r, c):   # 현재 칸 (r, c) 방문 중
	visited[r][c] = True
	if (r, c) == exit: return True
	if (r, c+1) == 0:  # 동쪽 이웃 칸이 빈 칸이고 미방문이라면
		if find_way_from_maze(r, c+1):
			M[r][c+1] = trace
			return True
	if (r, c) == 0:  # 남쪽 이웃 칸이 빈 칸이고 미방문이라면
		if find_way_from_maze(r+1, c):
			M[r][c+1] = trace
			return True
	if (r, c) == 0:  # 서쪽 이웃 칸이 빈 칸이고 미방문이라면
		if find_way_from_maze(r+1, c+1):
			M[r][c+1] = trace
			return True
	if (r, c) == 0:  # 북쪽 이웃 칸이 빈 칸이고 미방문이라면
		if find_way_from_maze(r+1, c+1):
			M[r][c+1] = trace
			return True
	return False

trace = '\u00B7'
n = int(input())
sx, sy, ex, ey = (int(x) for x in input().split())
M = []
# row 0 and n+1 are all 1's
# col 0 and n+1 are all 1's
for i in range(n):
    M.append([c for c in input()])

visited = [[False for _ in range(n)] for _ in range(n)]
M[sx][sy] = 's'
success = find_way_from_maze(sx, sy)
M[ex][ey] = 'e'

if success:
    for row in M:
        for c in row:
            if c == '1': 
                print('#', end="")
            elif c == '0':
                print(' ', end="")
            else:
                print(c, end="")
        print()
    print()
else:
    print("NO WAY!")
