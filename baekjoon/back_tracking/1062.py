import sys
input = sys.stdin.readline
# from itertools import combinations

max_cnt = 0
def solution():
    def check():
        # print(learn)
        tot = 0
        for word in words:
            flag = True
            for ch in word:
                if learn[ord(ch)-ord('a')] == 0:
                    flag = False
                    break
            if not flag:
                tot += 1
        return len(words) - tot
    def dfs(cnt, idx):
        global max_cnt
        if cnt > k-5:
            return
        # print("전",max_cnt)
        if cnt == k-5:
            max_cnt = max(max_cnt, check())
        # print("후",max_cnt)
        for i in range(idx, 26):
            if learn[i] == 0:
                learn[i] = 1
                dfs(cnt+1, i+1)
                learn[i] = 0
    n, k = map(int, input().split())
    words = [input().rstrip() for _ in range(n)]
    fixs = set("antatica")
    if k < 5:
        print(0)
        return
    elif k == 26:
        print(n)
        return
    learn = [0] * 26
    for fix in fixs:
        learn[ord(fix)-ord('a')] = 1
    dfs(0, 0)
    print(max_cnt)
solution()