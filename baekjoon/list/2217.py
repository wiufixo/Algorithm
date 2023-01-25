import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    ans = 0
    for i in range(len(arr)):
        ans = max(ans, arr[i] * n)
        n -= 1
    print(ans)
solution()
