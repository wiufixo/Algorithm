from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = 10 ** 7
v, e = map(int, input().split())
start = int(input())
links = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, w = map(int, input().split())
    links[a].append((b, w))
dist = [INF] * (v + 1)
dist[start] = 0
q = [(0, start)]
while q:
    cost, now = heappop(q)
    if cost != dist[now]:
        continue
    for nxt, nxt_cost in links[now]:
        tmp = dist[now] + nxt_cost
        if dist[nxt] > tmp:
            dist[nxt] = tmp
            heappush(q, (tmp, nxt))
for i in range(1, v + 1):
    print(dist[i] if dist[i] != INF else 'INF')