import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n, k = map(int, input().split())
    up = 1
    down = 1
    for i in range(k):
        up *= (n-i)
        down *= (k-i)
    print(up//down)
solution()