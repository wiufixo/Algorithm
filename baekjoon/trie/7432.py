import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    def add(arr):
        cur = root
        for folder in arr:
            if not folder in cur:
                cur[folder] = {}
            cur = cur[folder]
    def draw(cur, cnt):
        for key in sorted(cur.keys()):
            print(' '*cnt + key)
            draw(cur[key], cnt+1)
    n = int(input())
    root = {}
    for i in range(n):
        add(input().rstrip().split('\\'))
    draw(root, 0)
solution()