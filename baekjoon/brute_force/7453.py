import sys
input = sys.stdin.readline
from collections import Counter

def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a, b, c, d = zip(*arr)
    first = []
    second = []
    for i in range(n):
        for j in range(n):
            first.append(a[i]+b[j])
            second.append(c[i]+d[j])
    # print(first, second)
    cont = Counter(second)
    # print(cont)
    ans = 0
    for num in first:
        ans += cont[-num]
    print(ans)
solution()