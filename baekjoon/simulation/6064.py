import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    def find():
        k = x
        i = 0
        while k <= m * n:
            if (k - y) % n == 0:
                return k
            else:
                i += 1
                k = m * i + x
        return -1
    t = int(input())
    for _ in range(t):
        m, n, x, y = map(int, input().split())
        print(find())
solution()
            