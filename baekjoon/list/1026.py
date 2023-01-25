import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    tot = 0
    for x, y in zip(a,b):
        tot += x * y
    print(tot)
solution()