import sys
sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline

m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(a,b):
    if a == m-1 and b == n-1:
        return 1
    if dp[a][b] != -1:
        return dp[a][b]
    way = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if g[nx][ny] < g[a][b]:
            way += dfs(nx,ny)
    dp[a][b] = way
    return dp[a][b]
dp = [[-1] * n for _ in range(m)]
print(dfs(0,0))