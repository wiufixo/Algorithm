import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        s = input().rstrip()
        left = []
        right = []
        for ch in s:
            if ch == '<':
                if left:
                    right.append(left.pop())
            elif ch == '>':
                if right:
                    left.append(right.pop())
            elif ch == '-':
                if left:
                    left.pop()
            else:
                left.append(ch)
        print(''.join(left+list(reversed(right))))
            
solution()