import sys
input = sys.stdin.readline
def solution():
    word = input()
    dp = [0]*len(word)
    if word[0] == '0':
        print(0)
        return
    dp[0] = 1
    for i in range(1, len(word)):
        if word[i] != '0':
            dp[i] += dp[i-1]
        if i>1:
            if 10<=int(word[i-1:i+1])<=26:
                dp[i] += dp[i-2]
        else:
            if 10<=int(word[i-1:i+1])<=26:
                dp[i] += 1
    print(dp[-1]%1000000)
solution()