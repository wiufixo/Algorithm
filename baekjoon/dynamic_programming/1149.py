import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
ans = 10 ** 9
def solution():
    INF = 1001
    n = int(input())
    arr = [0]
    for i in range(n):
        arr.append(list(map(int, input().split())))
    dp = [[0,0,0] for _ in range(n+1)]
    dp[1][0] = arr[1][0]
    dp[1][1] = arr[1][1]
    dp[1][2] = arr[1][2]
    for i in range(2, n+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
    print(min(dp[n]))
solution()