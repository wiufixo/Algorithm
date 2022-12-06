import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
cnt = 0
def solution():
    def dfs(idx, tot, nums):
        global cnt
        if nums != 0 and idx == n and tot == target:
            # print(idx, tot, nums)
            cnt += 1
        if idx == n:
            return
        # for i in range(idx, len(arr)):
        #     dfs(i+1, tot+arr[i])
        dfs(idx+1, tot+arr[idx], nums+1)
        # print(arr[idx])
        dfs(idx+1, tot, nums)
    
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    dfs(0, 0, 0)
    print(cnt)
solution()