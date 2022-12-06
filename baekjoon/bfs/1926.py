from collections import deque
import sys
input = sys.stdin.readline
max_tot = 0
def solution():
    def bfs(a, b):
        global max_tot
        q = deque([(a, b)])
        g[a][b] = 0
        tot = 0
        while q:
            x, y = q.popleft()
            tot += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1:
                    g[nx][ny] = 0
                    q.append((nx, ny))
        max_tot = max(max_tot, tot)
                    
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
    print(max_tot)
    
solution()