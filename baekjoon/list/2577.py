import sys
input = sys.stdin.readline
def solution():
    a, b, c = int(input().rstrip()), int(input().rstrip()), int(input().rstrip())
    abc = a * b * c
    arr = [0 for _ in range(10)]
    for ch in str(abc):
        arr[int(ch)] += 1
    for a in arr:
        print(a)
solution()