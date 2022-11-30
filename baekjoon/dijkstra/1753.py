import heapq, sys
input = sys.stdin.readline

def solution():
    v, e = map(int,input().split())
    k = int(input())
    edges = [list(map(int, input().split())) for _ in range(e)]
    conns = [[] for _ in range(v+1)]
    for start, end, cost in edges:
        conns[start].append((end, cost))
    INF = 10**9
    dist = [INF] * (v+1)
    dist[k] = 0
    q = [(0,k)]
    while q:
        weight, node = heapq.heappop(q)
        if weight != dist[node]:
            continue
        for next_node, cost in conns[node]:
            next_cost = weight + cost
            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                heapq.heappush(q, (next_cost, next_node))
    for i in range(1, v+1):
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])
solution()