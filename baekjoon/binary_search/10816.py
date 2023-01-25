import sys, math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    def find(num):
        l = bisect_left(a, num)
        r = bisect_right(a, num)
        return r - l
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = int(input())
    b = list(map(int, input().split()))
    for num in b:
        print(find(num), end=" ")
solution()