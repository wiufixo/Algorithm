import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    def dfs(idx, cnt):
        if cnt == m:
            print(*ans)
        for i in range(1, n+1):
            if not check[i]:
                ans.append(i)
                check[i] = 1
                dfs(i+1, cnt+1)
                check[i] = 0
                ans.pop()
    n, m = map(int, input().split())
    check = [0] * (n+1)
    ans = []
    dfs(1, 0)
solution()