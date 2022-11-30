from collections import deque
from itertools import combinations
n, m = map(int, input().split())
# arr_p = [[0,0,0,0,0,0],[1,0,0,0,0,2],[1,1,1,0,0,2],[0,0,0,0,0,2]]
arr_p = [[int(i) for i in input().split()] for _ in range(n)]
# print(arr_p)
def bfs(a,b,arr):
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    q = deque([(a,b)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                q.append((nx,ny))
                arr[nx][ny] = 2
candi = []
viruses = []
for i in range(n):
    for j in range(m):
        if arr_p[i][j] == 0:
            candi.append((i,j))
        if arr_p[i][j] == 2:
            viruses.append((i,j))
candi_three = list(combinations(candi, 3))
res = 0
for walls in candi_three:
    arr = [[j for j in arr_p[i]] for i in range(len(arr_p))]
    cnt = 0
    for wall in walls:
        arr[wall[0]][wall[1]] = 1
    for virus in viruses:
        bfs(virus[0], virus[1], arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1
    res = max(res, cnt)
print(res)