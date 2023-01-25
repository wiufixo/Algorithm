import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
max_block = 0
def solution():
    def move(d, g):
        global max_block
        if d == 0:
            for j in range(n): # 열 고정
                idx = 0
                val = g[0][j]
                for i in range(1, n):
                    tmp = g[i][j]
                    if tmp == 0:
                        continue
                    if tmp == val:
                        g[i][j] = 0
                        g[idx][j] = 2 * val
                        max_block = max(max_block, 2 * val)
                        idx += 1
                        val = 0
                    else:
                        if val != 0:
                            idx += 1
                        g[i][j] = 0
                        g[idx][j] = tmp
                        val = tmp
        elif d == 1:
            for i in range(n): # 행 고정
                idx = n-1
                val = g[i][n-1]
                for j in range(n-2, -1, -1):
                    tmp = g[i][j]
                    if tmp == 0:
                        continue
                    if tmp == val:
                        g[i][j] = 0
                        g[i][idx] = 2 * val
                        max_block = max(max_block, 2 * val)
                        idx -= 1
                        val = 0
                    else:
                        if val != 0:
                            idx -= 1
                        g[i][j] = 0
                        g[i][idx] = tmp
                        val = tmp
        elif d == 2:
            for j in range(n): # 열 고정
                idx = n-1
                val = g[n-1][j]
                for i in range(n-2, -1, -1):
                    tmp = g[i][j]
                    if tmp == 0:
                        continue
                    if tmp == val:
                        g[i][j] = 0
                        g[idx][j] = 2 * val
                        max_block = max(max_block, 2 * val)
                        idx -= 1
                        val = 0
                    else:
                        if val != 0:
                            idx -= 1
                        g[i][j] = 0
                        g[idx][j] = tmp
                        val = tmp
        elif d == 3:
            for i in range(n): # 행 고정
                idx = 0
                val = g[i][0]
                for j in range(1, n):
                    tmp = g[i][j]
                    if tmp == 0:
                        continue
                    if tmp == val:
                        g[i][j] = 0
                        g[i][idx] = 2 * val
                        max_block = max(max_block, 2 * val)
                        idx += 1
                        val = 0
                    else:
                        if val != 0:
                            idx += 1
                        g[i][j] = 0
                        g[i][idx] = tmp
                        val = tmp
    def dfs(cnt, g):
        temp = copy.deepcopy(g)
        if cnt == 5:
            # print(g)
            return
        for i in range(4):
            move(i, temp)
            dfs(cnt+1, temp)
            temp = copy.deepcopy(g)
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    
    global max_block
    for i in range(n):
        for j in range(n):
            max_block = max(max_block, g[i][j])
    # n = 3
    # g = [
    #     [2,2,2], [4,4,4], [8,8,8]
    # ]
    dx = [-1,0,1,0] # 0 1 2 3
    dy = [0,1,0,-1] # 상하좌우
    dfs(0, g)
    print(max_block)
    
solution()