import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    for _ in range(t):
        word = input().strip()
        start = 0
        end = len(word)-1
        ans = 0
        while start < end:
            if word[start] == word[end]:
                start += 1
                end -= 1
                continue
            else:
                if start == 0:
                    if word[:end] == word[end-1::-1] or word[start+1:] == word[end:start:-1]:
                        ans = 1
                        break
                    ans = 2
                    break
                else:
                    if word[start:end] == word[end-1:start-1:-1] or word[start+1:end+1] == word[end:start:-1]:
                        ans = 1
                        break
                    ans = 2
                    break
        print(ans)
solution()




