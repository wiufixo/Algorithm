import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    if n == 1:
        print()
        return
    k = 2
    while n != 1:
        if n % k == 0:
            print(k)
            n //= k
        else:
            k += 1
solution()