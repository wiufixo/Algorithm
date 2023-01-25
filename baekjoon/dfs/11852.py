import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    INF = 10 ** 6 + 1
    dp = [INF for i in range(n+1)]
    prev = [0 for i in range(n+1)]
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        prev[i] = i-1
        if i % 3 == 0:
            if dp[i//3] + 1 < dp[i]:
                dp[i] = dp[i//3] + 1
                prev[i] = i//3
        if i % 2 == 0:
            if dp[i//2] + 1 < dp[i]:
                dp[i] = dp[i//2] + 1
                prev[i] = i//2
    prv = prev[n]
    ans = [n]
    while prv != 0:
        ans.append(prv)
        prv = prev[prv]
    print(dp[n])
    print(*ans)
solution()