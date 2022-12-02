import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip()
    arr = [0] * 26
    for ch in s:
        idx = ord(ch)-ord('a')
        arr[idx] += 1
    print(*arr)
        
solution()