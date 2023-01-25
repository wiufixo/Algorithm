import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    dp = [[0,0] for _ in range(n+1)]
    arr = [0] * (n+1)
    for i in range(1,n+1):
        temp = int(input())
        arr[i] = temp
        dp[i][0] += temp
    for i in range(2,n+1):
        dp[i][0] += max(dp[i-2][1] + arr[i-1], dp[i-1][1])
        dp[i][1] += dp[i-1][0]
    print(dp[n][0])
solution()