import sys
input = sys.stdin.readline
def solution():
    while True:
        ans = True
        stk = []
        line = input().rstrip()
        if line == '.':
            break
        for ch in line:
            if ch == '[' or ch == '(':
                stk.append(ch)
            elif ch == ']' or ch == ')':
                rev_ch = '[' if ch == ']' else '('
                if not stk or stk[-1] != rev_ch:
                    ans = False
                    break
                stk.pop()
        if stk:
            ans = False
        print("no" if not ans else "yes")
            
solution()