import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    def recur(n, cnt):
        if cnt == 1:
            return n % c
        temp = recur(n, cnt//2)
        if cnt % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * n) % c
    a, b, c = map(int, input().split())
    print(recur(a, b))
solution()
