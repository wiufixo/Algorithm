from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    sec = [0]+list(map(int,input().split()))
    conn = [[] for _ in range(n+1)]
    in_cnt = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    for i in range(k):
        a,b = map(int, input().split())
        conn[a].append(b)
        in_cnt[b] += 1
    target = int(input())
    q = deque()
    for i in range(1, n+1):
        if in_cnt[i] == 0:
            q.append(i)
            dp[i] = sec[i]
    while q:
        curr = q.popleft()
        for con in conn[curr]:
            in_cnt[con] -= 1
            dp[con] = max(dp[curr]+sec[con], dp[con])
            if in_cnt[con] == 0:
                q.append(con)
    print(dp[target])