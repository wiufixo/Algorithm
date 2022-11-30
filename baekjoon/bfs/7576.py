from collections import deque
import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(m)]
    ik = []
    not_ik = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1:
                ik.append((i,j))
            if g[i][j] == 0:
                not_ik.append((i,j))
    if not ik:
        print(-1)
        return
    if not not_ik:
        print(0)
        return
    not_ik_cnt = len(not_ik)
    max_days = 0
    cnt = 0
    q = deque()
    for x, y in ik:
        q.append((x, y, 0))
    while q:
        x, y, days = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if g[nx][ny] == -1 or g[nx][ny] == 1:
                continue
            g[nx][ny] = 1
            cnt += 1
            max_days = max(max_days, days+1)
            q.append((nx, ny, days+1))
    # print(g)
    if cnt != not_ik_cnt:
        print(-1)
        return
    else:
        print(max_days)
solution()