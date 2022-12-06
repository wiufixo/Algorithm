from collections import deque
import sys
input = sys.stdin.readline
def solution():
    def bfs(a, b):
        q = deque([(a, b)])
        visited[a][b] = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1 and not visited[nx][ny]:
                    g[nx][ny] = g[x][y] + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    
    n, m = map(int, input().split())
    g = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    bfs(0,0)
    print(g[n-1][m-1])
solution()