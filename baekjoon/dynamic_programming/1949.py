# solution()
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    def dfs(cur):
        visited[cur] = 1
        for child in links[cur]:
            if visited[child] == 0:
                dfs(child)
                dp[cur][0] += dp[child][1]
                dp[cur][1] += max(dp[child][0],dp[child][1])
    n = int(input())
    # n = 7
    dp = [[0,0] for _ in range(n+1)]
    links = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    # arr = [
    #     [1,2], [2,3], [4,3], [4,5], [6,2], [6,7]
    # ]
    # arr_ = [
    #     1000,3000,4000,1000,2000,2000,7000
    # ]
    # for i in range(n):
    #     dp[i+1][0] = arr_[i]
    # for x, y in arr:
    #     links[x].append(y)
    #     links[y].append(x)
    for i, val in enumerate(map(int, input().split())):
        dp[i+1][0] = val
    for i in range(n-1):
        x, y = map(int, input().split())
        links[x].append(y)
        links[y].append(x)
    dfs(1)
    print(max(dp[1]))

solution()