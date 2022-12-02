import math, sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    def is_prime(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    n = int(input())
    ac = [0, 0] + [1] * (n-1)
    arr = []
    for i in range(2, int(math.sqrt(n))+1):
        if ac[i]:
            k = 2
            while i * k <= n:
                ac[i * k] = 0
                k += 1
    # print(ac)
    for i in range(len(ac)):
        if ac[i]:
            arr.append(i)
    # print(arr)
    
    l, r, total = 0, 0, 0
    cnt = 0
    while True:
        if total < n:
            if r == len(arr):
                break
            total += arr[r]
            r += 1
        else:
            if total == n:
                cnt += 1
            total -= arr[l]
            l += 1
    print(cnt)
solution()