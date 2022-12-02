import sys
from collections import deque
input = sys.stdin.readline
def solution():
    s = input().rstrip()
    m = int(input())
    left = deque(list(s))
    right = deque()
    # cur = len(s)
    for i in range(m):
        q = input().rstrip().split()
        if q[0] == 'L':
            if left:
                right.appendleft(left.pop())
        elif q[0] == 'D':
            if right:
                left.append(right.popleft())
        elif q[0] == 'B':
            if left:
                left.pop()
        else: # q[0] == 'P':
            left.append(q[1])
    print(''.join(left + right))
solution()