from collections import deque
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    arr = deque(list(range(1, n+1)))
    ans = []
    while arr:
        for _ in range(k-1):
            arr.append(arr.popleft())
        ans.append(arr.popleft())
    print(str(ans).replace('[', '<').replace(']', '>'))
    # print('<'+', '.join(map(str, ans))+'>')
solution()
