import sys, math
input = sys.stdin.readline

def solution():
    def min_tree(node, start, end):
        if start == end:
            min_arr[node] = arr[start]
            return min_arr[node]
        
        mid = (start+end)//2
        min_arr[node] = min(min_tree(2*node, start, mid), min_tree(2*node+1, mid+1, end))
        return min_arr[node]
    def max_tree(node, start, end):
        if start == end:
            max_arr[node] = arr[start]
            return max_arr[node]
        mid = (start+end)//2
        max_arr[node] = max(max_tree(2*node, start, mid), max_tree(2*node+1, mid+1, end))
        return max_arr[node]
    def min_query(node, start, end, left, right):
        if right < start or left > end:
            return INF
        if left <= start and end <= right:
            return min_arr[node]
        mid = (start+end)//2
        return min(min_query(2*node, start, mid, left, right), min_query(2*node+1, mid+1, end, left, right))
    def max_query(node, start, end, left, right):
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return max_arr[node]
        mid = (start+end)//2
        return max(max_query(2*node, start, mid, left, right), max_query(2*node+1, mid+1, end, left, right))
    n, m = map(int, input().split())
    arr = [0]
    for i in range(n):
        arr.append(int(input()))
    min_arr = [0] * (2 ** (int(math.log2(n))+2))
    max_arr = [0] * (2 ** (int(math.log2(n))+2))
    INF = 10 ** 10
    min_tree(1, 1, n)
    max_tree(1, 1, n)
    for i in range(m):
        a, b = map(int, input().split())
        print(min_query(1, 1, n, a, b), max_query(1, 1, n, a, b))
solution()
