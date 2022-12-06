from collections import deque
import sys, copy
input = sys.stdin.readline
def solution():
    def bfs():
        q = deque(fires)
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == '.':
                    g[nx][ny] = g[x][y] + 1
                    q.append((nx, ny))
    def miro(a, b):
        q = deque([(a, b, 0)])
        visited[a][b] = 1
        while q:
            x, y, time = q.popleft()
            if x == 0 or y == 0 or x == n-1 or y == m-1:
                return time + 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#' and not visited[nx][ny]:
                    if g[nx][ny] == '.': # 불과 단절된 곳
                        visited[nx][ny] = 1
                        q.append((nx, ny, time+1))
                    else: # 불 퍼질 수 있는 곳
                        if g[nx][ny] > time + 1:
                            visited[nx][ny] = 1
                            q.append((nx, ny, time+1))
        return -1
                    
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    g = copy.deepcopy(graph)
    visited = [[0] * m for _ in range(n)]
    x, y = 0, 0 # 출발점
    fires = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'J':
                x, y = i, j
                g[i][j] = '.'
            if g[i][j] == 'F':
                fires.append((i,j))
                g[i][j] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    bfs()
    ans = miro(x, y)
    print("IMPOSSIBLE" if ans == -1 else ans)
solution()