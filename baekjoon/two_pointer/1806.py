import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    # n, s = 10, 15
    # arr = [5,1,3,5,10,7,4,9,2,8]
    l, r = 0, 0
    tot = 0
    length = 10**6
    while l<n:
        if tot < s:
            if r == n:
                break
            tot += arr[r]
            r += 1
        else: # 이상일때
            length = min(length, r - l)
            tot -= arr[l]
            l += 1
    print(length if length != 10**6 else 0)
solution()
