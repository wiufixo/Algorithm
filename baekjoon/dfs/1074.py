import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
cnt = -1
def solution():
    def recur(k,x,y):
        global cnt
        if k == 0:
            cnt += 1
            # if x == r and y == c:
            print(cnt)
            return
        size = 2**(k-1)
        nx = x + size
        ny = y + size
        if r < nx and c < ny:
            recur(k-1, x, y)
        elif r < nx and ny <= c:
            cnt += size * size
            recur(k-1, x, ny)
        elif nx <= r and c < ny:
            cnt += size * size * 2
            recur(k-1, nx, y)
        elif nx <= r and ny <= c:
            cnt += size * size * 3
            recur(k-1, nx, ny)
    n, r, c = map(int, input().split())
    recur(n,0,0)
solution()
