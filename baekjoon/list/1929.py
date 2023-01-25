import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    m, n = map(int, input().split())
    arr = [0, 0] + [1] * (n-1)
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]:
            for j in range(i * 2, n + 1, i):
                arr[j] = 0
            # k = 2
            # while i * k < n + 1:
            #     arr[i * k] = 0
            #     k += 1
    for i in range(m, n+1):
        if arr[i]:
            print(i)
solution()