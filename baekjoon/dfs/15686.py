import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
min_chk_dist = 10 ** 5
def solution():
    def check():
        tot_dist = 0
        for h_x, h_y in homes:
            min_dist = 10 ** 3
            for c_x, c_y in alive:
                min_dist = min(min_dist, abs(h_x-c_x) + abs(h_y-c_y))
            tot_dist += min_dist
        return tot_dist
    def dfs(cnt, idx):
        global min_chk_dist
        if cnt == m:
            # print(alive)
            min_chk_dist = min(min_chk_dist, check())
            return
        for i in range(idx, len(chks)):
            alive.append(chks[i])
            dfs(cnt+1, i+1)
            alive.pop()
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    chks = []
    homes = []
    for i in range(n):
        for j in range(n):
            if g[i][j] == 2:
                chks.append((i,j))
            if g[i][j] == 1:
                homes.append((i,j))
    alive = []
    dfs(0, 0)
    print(min_chk_dist)
solution()