import sys
input = sys.stdin.readline

def solution():
    str1 = input().rstrip()
    str2 = input().rstrip()
    m = len(str1)
    n = len(str2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    res = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                if i == 1 or j == 1:
                    dp[i][j] = 1
                else:
                    if str1[i-2] == str2[j-2]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for i in range(1,m+1):
        for j in range(1,n+1):
            res = max(dp[i][j],res)
    print(res)
solution()