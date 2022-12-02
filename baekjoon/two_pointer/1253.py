import math, sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    def find_good(i,num):
        l, r, = 0, n-1
        while l < r:
            if r == i:
                r -= 1
                continue
            elif l == i:
                l += 1
                continue
            total = arr[l] + arr[r]
            if total < num:
                l += 1
            elif total > num:
                r -= 1
            else: # total == num:
                return True
        return False
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    cnt = 0
    for i,num in enumerate(arr):
        if find_good(i,num):
            cnt += 1
    print(cnt)
solution()