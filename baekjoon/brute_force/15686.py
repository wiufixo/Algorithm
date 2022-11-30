from itertools import combinations

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))
INF = 1e4
def get_dist(chicks, g):
    # print(chicks)
    dist = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                h = INF
                for x, y in chicks:
                    h = min(h, abs(i-x)+abs(j-y))
                
                dist += h
    return dist
chicks = []
ans = INF
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            chicks.append((i,j))
chicks = list(combinations(chicks, m))
for combi in chicks:
    ans = min(ans, get_dist(combi, g))
print(ans)