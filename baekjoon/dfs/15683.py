import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
min_see = 100
def solution():
    def fill(ds, x, y, cnt):
        chk = 0
        for d in ds:
            nx = x
            ny = y
            while True:
                # print(d)
                nx += dx[d]
                ny += dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if tmp[nx][ny] == 6:
                        break
                    if tmp[nx][ny] == 0:
                        tmp[nx][ny] = cnt+7
                        chk += 1
                else:
                    break
        return chk
    def out(ds, x, y, cnt):
        for d in ds:
            nx = x
            ny = y
            while True:
                nx += dx[d]
                ny += dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if tmp[nx][ny] == 6:
                        break
                    if tmp[nx][ny] == cnt+7:
                        tmp[nx][ny] = 0
                else:
                    break
    def dfs(cnt, emp):
        global min_see
        if cnt == len(cms):
            min_see = min(min_see, emp)
            return
        num, x, y = cms[cnt]
        for ds in dirt[num]:
            f = fill(ds, x, y, cnt)
            dfs(cnt+1, emp-f)
            out(ds, x, y, cnt)
    n, m = map(int,input().split())
    tmp = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dirt = [0,[[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]
    cms = []
    emp = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                emp += 1
            if tmp[i][j] != 0 and tmp[i][j] != 6:
                cms.append((tmp[i][j],i,j))
    dfs(0, emp)
    print(min_see)
solution()