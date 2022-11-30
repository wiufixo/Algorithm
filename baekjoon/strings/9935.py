import sys
input = sys.stdin.readline

def solution():
    words = input().rstrip()
    bomb = input().rstrip()
    stack = []
    for word in words:
        stack.append(word)
        if len(stack) >= len(bomb):
            if "".join(stack[-len(bomb):]) == bomb:
                for i in range(len(bomb)):
                    stack.pop()
    if not stack:
        print("FRULA")
    else:
        print("".join(stack))
solution()