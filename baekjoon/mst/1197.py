import sys
input = sys.stdin.readline
import heapq

def solution():
    v, e = map(int, input().split())
    links = [[] for _ in range(v+1)]
    for i in range(e):
        start, end, cost = map(int, input().split())
        links[start].append((cost,end))
        links[end].append((cost,start))
    visited = [False] * (v+1)
    q = []
    heapq.heappush(q, (0,1))
    max_dist = 0
    while q:
        cost, now = heapq.heappop(q)
        if visited[now]:
            continue
        visited[now] = True
        max_dist += cost
        for next_cost, next_ in links[now]:
            if visited[next_]:
                continue
            heapq.heappush(q, (next_cost, next_))
    print(max_dist)
solution()