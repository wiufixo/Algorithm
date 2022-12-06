from collections import deque
import sys, copy
input = sys.stdin.readline
def solution():
    def bfs(a, y):
        q = deque([(a, 0)])
        visited[a] = 1
        while q:
            x, time = q.popleft()
            if x == y:
                print(time)
                break
            for i in [x+1, x-1, 2*x]:
                x = i
                if 0 <= x <= 100000 and not visited[x]:
                    q.append((x, time+1))
                    visited[x] = 1
    x, y = map(int, input().split())
    visited = [0] * 100001
    bfs(x, y)
solution()