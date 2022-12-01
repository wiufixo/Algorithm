import sys
input = sys.stdin.readline

def solution():
    # for i in range(1, n+1):
    #     cnt = i & (-i)
    #     tot = 0
    #     for j in range(i, i-cnt, -1):
    #         tot += j
    #     save_sum[i] = tot
    def from_first_sum(k):
        total = 0
        while k > 0:
            total += save_sum[k]
            k -= k & (-k)
        return total
    def update(k, diff):
        while k <= n:
            save_sum[k] += diff
            k += k & (-k)
    n, m, k = map(int, input().split())
    arr = [0]
    save_sum = [0] * (n+1)
    for i in range(1, n+1):
        num = int(input())
        arr.append(num)
        update(i, num)
    for i in range(m+k):
        a, b, c = map(int, input().split())
        if a == 1:
            diff = c-arr[b]
            arr[b] = c
            update(b, diff)
        else:
            print(from_first_sum(c) - from_first_sum(b-1))
solution()