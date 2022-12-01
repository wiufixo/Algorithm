def solution():
    def dfs(k, arr):
        arr[k] = -2
        for i in range(len(arr)):
            if arr[i] == k:
                dfs(i, arr)
    n = int(input())
    arr = list(map(int, input().split()))
    links = [[] for _ in range(n)]
    root = -1
    for i in range(len(arr)):
        if arr[i] != -1:
            links[arr[i]].append(i)
        else:
            root = i
    k = int(input())
    dfs(k, arr)
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != -2 and i not in arr:
            cnt += 1
    if k == root:
        print(0)
    else:
        print(cnt)
solution()