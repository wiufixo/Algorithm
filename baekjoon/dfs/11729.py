import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    def count(k):
        if k == 1:
            return 1
        return 2 * count(k-1) + 1
    def recur(a,b,c,k):
        if k == 1:
            print(a,c)
            return
        recur(a, c, b, k-1)
        print(a, c)
        recur(b, a, c, k-1)
    n = int(input())
    print(count(n))
    recur(1,2,3,n)
solution()
