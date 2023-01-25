import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    def find(num):
        l, r = 0, len(a)-1
        while l <= r:
            mid = (l + r) // 2
            if num > a[mid]:
                l = mid + 1
            elif num < a[mid]:
                r = mid - 1
            else: # 찾았다
                return 1
        return 0
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = int(input())
    b = list(map(int, input().split()))
    for num in b:
        print(find(num))
solution()