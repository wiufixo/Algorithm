import sys, math
input = sys.stdin.readline
def solution():
    n = input().rstrip()
    arr = [0] * 10
    for ch in n:
        if ch == '6' or ch == '9':
            arr[int(6)] += 1
        else:
            arr[int(ch)] += 1
    arr[6] = arr[6] // 2 if arr[6] % 2 == 0 else arr[6] // 2 + 1
    print(max(arr))
solution()