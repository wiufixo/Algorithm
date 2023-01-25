import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    INF = 10 ** 6 + 1
    dp = [INF] * (n+1)
    dp[1] = 0
    # dp[2] = 1
    for i in range(2, n+1):
        arr = set()
        if i % 3 == 0:
            arr.add(i//3)
        if i % 2 == 0:
            arr.add(i//2)
        arr.add(i-1)
        for k in arr:
            dp[i] = min(dp[k], dp[i])
        dp[i] += 1
    print(dp[n])
solution()
