import sys, math
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    x = int(input())
    l, r = 0, len(arr)-1
    cnt = 0
    while l < r:
        tot = arr[l] + arr[r]
        if tot < x:
            l += 1
        else:
            if tot == x:
                cnt += 1
            r -= 1
    print(cnt)
solution()