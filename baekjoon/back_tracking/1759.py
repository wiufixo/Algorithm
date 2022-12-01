import sys
# input = sys.stdin.readline
def solution():
    # l, c = 4, 6
    # ch = list("atcisw")
    l, c = map(int, input().split())
    ch = input().split()
    ch.sort()
    mo_list = list("aeiou")
    def back(cur,idx,re):
        if len(re) == l:
            mo_cnt, ja_cnt = 0, 0
            for r in re:
                if r in mo_list:
                    mo_cnt += 1
                else:
                    ja_cnt += 1
            if mo_cnt >= 1 and ja_cnt >= 2:
                print(re)
                return
        for i in range(idx,c):
            back(cur+1, i+1, re+ch[i])
    back(1,0,"")
solution()

