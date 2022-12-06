from collections import deque
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = deque()
    for _ in range(n):
        q = input().split()
        if q[0] == 'push':
            arr.append(q[1])
        elif q[0] == 'pop':
            print(-1 if not arr else arr.popleft())
        elif q[0] == 'size':
            print(len(arr))
        elif q[0] == 'empty':
            print(1 if not arr else 0)
        elif q[0] == 'front':
            print(-1 if not arr else arr[0])
        elif q[0] == 'back':
            print(-1 if not arr else arr[-1])
solution()