import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    def p_num(k):
        if k == 1:
            return False
        for i in range(2, int(math.sqrt(k))+1):
            if k % i == 0:
                return False
        return True
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in arr:
        if p_num(i):
            cnt += 1
    print(cnt)
solution()