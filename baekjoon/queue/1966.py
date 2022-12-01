from collections import deque

def solution():
    t = int(input())
    # t = 1
    for _ in range(t):
        n, cur = map(int, input().split())
        impots = list(map(int, input().split()))
        # n, cur = 6, 0
        # impots = [1,1,9,1,1,1]
        q = deque(impots)
        count = 0
        while q:
            maxi = max(q)
            now = q.popleft()
            cur -= 1
            if now == maxi:
                count += 1
                if cur < 0:
                    print(count)
                    break
            else:
                q.append(now)
                if cur < 0:
                    cur = len(q)-1
solution()

