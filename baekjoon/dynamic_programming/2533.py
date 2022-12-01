import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def solution():
    def dfs(cur):
        visited[cur] = 1
        dp[cur][0] = 1
        for next_node in links[cur]:
            if visited[next_node]:
                continue
            dfs(next_node)
            dp[cur][0] += min(dp[next_node][0], dp[next_node][1])
            dp[cur][1] += dp[next_node][0]
    n = int(input())
    links = [[] for _ in range(n+1)]
    dp = [[0,0] for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(n-1):
        u, v = map(int, input().split())
        links[u].append(v)
        links[v].append(u)
    # print(links)
    dfs(1)
    print(min(dp[1]))
    # print(dp)
solution()
