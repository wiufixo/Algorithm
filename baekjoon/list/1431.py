import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
def solution():
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    nums.sort(key = lambda x:(len(x), sum([int(ch) for ch in x if not ch.isalpha()]), x))
    for num in nums:
        print(num)
solution()
