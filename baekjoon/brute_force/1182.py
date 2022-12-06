from itertools import combinations
import sys, copy, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    # def dfs():
    
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1,len(arr)+1):
        for combi in combinations(arr, i):
            if sum(combi) == target:
                cnt += 1
    print(cnt)
solution()