import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n, k = map(int, input().split())
    coins = list(reversed([int(input()) for _ in range(n)]))
    i = 0
    cnt = 0
    while k != 0:
        mo = k // coins[i]
        if mo > 0:
            k %= coins[i]
            cnt += mo
        i += 1
    print(cnt)
solution()