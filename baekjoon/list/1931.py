import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    arr = []
    for i in range(n):
        l, r = map(int, input().split())
        arr.append((l,r))
    arr.sort(key=lambda x:x[0])
    arr.sort(key=lambda x:x[1])
    k, cnt = 0, 0
    for s, e in arr:
        if k <= s:
            cnt += 1
            k = e
    print(cnt)
solution()

