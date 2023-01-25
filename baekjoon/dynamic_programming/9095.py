import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    INF = 10 ** 6 + 1
    dp = [0] * (10+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4,10+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    t = int(input())
    for _ in range(t):
        print(dp[int(input())])
solution()