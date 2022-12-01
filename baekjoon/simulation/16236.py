from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def solution():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    def bfs(a,b):
        visited = [[False] * n for _ in range(n)]
        q = deque([[a,b,0]])
        visited[a][b] = True
        eat = []
        while q:
            x, y, dist = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if g[nx][ny] > size:
                    continue
                if visited[nx][ny]:
                    continue
                if g[nx][ny] < size and g[nx][ny] != 0:
                    eat.append([dist+1, nx, ny])
                visited[nx][ny] = True
                q.append([nx,ny,dist+1])
        if eat:
            eat.sort()
            eat = eat[0]
        return eat
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    time = 0
    size = 2
    eated = 0
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 9:
                x, y = i, j
    while True:
        fish = bfs(x, y)
        if not fish:
            print(time)
            break
        dist, i, j = fish
        time += dist
        g[x][y] = 0
        g[i][j] = 9
        eated += 1
        if eated == size:
            size += 1
            eated = 0
        x, y = i, j
solution()
