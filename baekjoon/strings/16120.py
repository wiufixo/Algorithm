import sys
input = sys.stdin.readline

def solution():
    word = input().strip()
    stack = []
    for w in word:
        stack.append(w)
        if len(stack) >= 4:
            if "".join(stack[-4:]) == "PPAP":
                for i in range(4):
                    stack.pop()
                stack.append("P")
    if len(stack) == 1 and stack[0] == 'P':
        print("PPAP")
    else:
        print("NP")
solution()
