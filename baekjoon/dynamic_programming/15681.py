import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    def dfs(cur):
        visited[cur] = 1
        for child in links[cur]:
            if visited[child] == 0:
                dfs(child)
                dp[cur] += dp[child]
    # v, r, q = 9, 5, 3
    v, r, q = map(int, input().split())
    links = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    dp = [1] * (v+1)
    for i in range(v-1):
        x, y = map(int, input().split())
        links[x].append(y)
        links[y].append(x)
    # arr = [
    #     [1,3], [4,3], [5,4], [5,6], [6,7], [2,3], [9,6], [6,8]
    # ]
    # for x, y in arr:
    #     links[x].append(y)
    #     links[y].append(x)
    # query = [5,4,8]
    # print(links)
    dfs(r)
    for i in range(q):
        print(dp[int(input())])
    # for i in query:
    #     print(dp[i])
solution()