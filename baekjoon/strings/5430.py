import sys
input = sys.stdin.readline
from collections import deque

def solution():
    t = int(input())
    for _ in range(t):
        p = input().strip()
        n = int(input())
        arr = input().strip()
        arr = arr[1:-1].split(',')
        if n == 0:
            q = deque()
        else:
            q = deque(arr)
        rev_cnt = 0
        flag = False
        for w in p:
            if w == 'R':
                if rev_cnt == 0:
                    rev_cnt = 1
                else:
                    rev_cnt = 0
            else:
                if not q:
                    flag = True
                    print('error')
                    break
                if rev_cnt == 0:
                    q.popleft()
                else:
                    q.pop()
        if flag:
            continue
        if rev_cnt == 0:
            print("["+",".join(q)+"]")
        else:
            print("["+",".join(reversed(q))+"]")
solution()
