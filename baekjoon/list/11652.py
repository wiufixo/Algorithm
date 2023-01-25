from collections import Counter
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    cnts = list(dict(Counter(arr)).items())
    cnts.sort(key=lambda x:(-x[1],x[0]))
    print(cnts[0][0])
solution()