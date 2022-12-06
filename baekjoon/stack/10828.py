import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    stk = []
    for i in range(n):
        q = input().split()
        if q[0] == 'push':
            stk.append(q[1])
        elif q[0] == 'pop':
            if stk:
                print(stk.pop())
            else:
                print(-1)
        elif q[0] == 'size':
            print(len(stk))
        elif q[0] == 'empty':
            print(1 if not stk else 0)
        elif q[0] == 'top':
            if stk:
                print(stk[-1])
            else:
                print(-1)
solution()
