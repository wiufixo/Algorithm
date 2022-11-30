import sys
input = sys.stdin.readline

n = int(input())
def solution(n):
    # if n == 1 or n == 3:
    #     return 0
    # if n == 2:
    #     return 3
    dp = [0]*(31)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] += dp[i-2]*3
        j = i-4
        while j >= 0:
            dp[i] += dp[j]*2
            j -= 2
        # for j in range(0, i-2, 2):
        #     dp[i] += dp[j]*2
    print(dp[n])
solution(n)