from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def main(INF):
    def dikstra(start, end, n):
        dist = [INF] * (n + 1)
        dist[start] = 0
        q = [(0, start)]
        while q:
            cost, now = heappop(q)
            if dist[now] != cost:
                continue
            for nxt, nxt_cost in links[now]:
                tmp = dist[now] + nxt_cost
                if dist[nxt] > tmp:
                    dist[nxt] = tmp
                    heappush(q, (tmp, nxt))
        return dist[end]
    n, e = map(int, input().split())
    links = [[] for _ in range(n + 1)]
    for i in range(e):
        a, b, c = map(int, input().split())
        links[a].append((b, c))
        links[b].append((a, c))
    v1, v2 = map(int, input().split())
    mid = dikstra(v1, v2, n)
    if mid == INF:
        return -1
    a = dikstra(1, v1, n) + mid + dikstra(v2, n, n)
    b = dikstra(1, v2, n) + mid + dikstra(v1, n, n)
    if a >= INF and b >= INF:
        return -1
    return min(a, b)
print(main(987654321))