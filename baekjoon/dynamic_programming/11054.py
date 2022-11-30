import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    arr_rev = [arr[i] for i in range(len(arr)-1, -1, -1)]
    # print(arr, arr_rev)
    dp_up = [1] * (n)
    dp_down = [1] * (n)
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp_up[i] = max(dp_up[j]+1, dp_up[i])
            if arr_rev[j] < arr_rev[i]:
                dp_down[i] = max(dp_down[j]+1, dp_down[i])
    re = 0
    for i in range(n):
        re = max(dp_up[i] + dp_down[-i-1], re)
    print(re-1)
solution()
