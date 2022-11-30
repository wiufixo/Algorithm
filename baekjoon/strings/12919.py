import sys
input = sys.stdin.readline
from collections import deque

ans = False
def solution():
    s = input().rstrip()
    t = input().rstrip()
    t_list = deque(list(t))
    def recur(q, length):
        global ans
        # if ans:
        #     return
        if len(q) == length:
            if "".join(q) == s:
                ans = True
            return
        start = q[0]
        end = q[-1]
        if start != 'B' and end =='A':
            cur = q.pop()
            recur(q, length)
            q.append(cur)
        if start == 'B' and end != 'A':
            cur = q.popleft()
            q.reverse()
            recur(q, length)
            q.append(cur)
            q.reverse()
        if start == 'B' and end == 'A':
            
            cur = q.pop()
            recur(q, length)
            q.append(cur)
            
            cur = q.popleft()
            q.reverse()
            recur(q, length)
            q.append(cur)
            q.reverse()
    recur(t_list, len(s))
    if ans:
        print(1)
    else:
        print(0)
solution()

