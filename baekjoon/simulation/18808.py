import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
ans = 0
def solution():
    def do(stk, r, c, x, y):
        global ans
        fills = 0
        for i in range(r):
            for j in range(c):
                if stk[i][j] == 1:
                    g[x+i][y+j] = 1
                    fills += 1
        ans += fills
    def compare(stk, r, c, x, y):
        for i in range(r):
            for j in range(c):
                if stk[i][j] == 1 and g[x+i][y+j] == 1:
                    return False
        return True
    def check(stk, r, c):
        for i in range(n-r+1):
            for j in range(m-c+1):
                if compare(stk, r, c, i, j):
                    do(stk, r, c, i, j)
                    return True
        return False
    
    n, m, k = map(int, input().split())
    g = [[0]*m for _ in range(n)]
    for i in range(k):
        r, c = map(int, input().split())
        stk = [list(map(int, input().split())) for _ in range(r)]
        cnt = 0
        while cnt < 4:
            if check(stk, r, c):
                break
            stk = [k[::-1] for k in zip(*stk)]
            r, c = c, r
            cnt += 1
    print(ans)
solution()
