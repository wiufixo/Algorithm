import sys
input = sys.stdin.readline
def solution():
    word = ' '+input().rstrip()
    n = int(input())
    str_list = []
    for _ in range(n):
        str_list.append(input().rstrip())
    
    dp = [0] * (len(word))
    dp[0] = 1
    for i in range(1, len(word)+1):
        for string in str_list:
            if i >= len(string):
                # print(word[i-len(string)+1:i+1], string)
                if word[i-len(string)+1:i+1] == string and dp[i-len(string)] == 1:
                    dp[i] = 1
    print(dp[len(word)-1])
solution()
