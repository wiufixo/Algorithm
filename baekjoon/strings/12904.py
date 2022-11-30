import sys
input = sys.stdin.readline
from collections import deque

def solution():
    s = input().rstrip()
    t = input().rstrip()
    flag = 0
    t_list = deque(list(t))
    while len(t_list) > len(s):
        cur = t_list.pop()
        if cur == 'B':
            t_list.reverse()
    if "".join(t_list) != s:
        print(0)
    else:
        print(1)
    #     if flag == 0:
    #         cur = t_list.pop()
    #         if cur == 'A':
    #             continue
    #         else:
    #             flag = 1
            
    #     else:
    #         cur = t_list.popleft()
    #         if cur == 'A':
    #             continue
    #         else:
    #             flag = 0
    
    # if flag == 1:
    #     t_list.reverse()
        
    # if "".join(t_list) != s:
    #     print(0)
    # else:
    #     print(1)
    
solution()
