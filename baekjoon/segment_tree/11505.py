import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**8)
DIV = 1000000007

def solution():
    def tree_init(node, start, end):
        if start == end:
            # print(node,start)
            tree[node] = arr[start]
            return tree[node]
        mid = (start+end)//2
        tree[node] = tree_init(2*node, start, mid) * tree_init(2*node+1, mid+1, end) % DIV
        return tree[node]
    def update(node, start, end, target, value):
        if target < start or end < target:
            return
        if start == end:
            tree[node] = value
            # arr[target] = value
            return
        mid = (start+end)//2
        update(2*node, start, mid, target, value)
        update(2*node+1, mid+1, end, target, value)
        tree[node] = tree[2*node] * tree[2*node+1] % DIV
        # tree[node] = tree_init(2*node, start, mid) * tree_init(2*node+1, mid+1, end)
    def query(node, start, end, left, right):
        if right < start or end < left:
            return 1
        if left <= start and end <= right:
            return tree[node]
        mid = (start+end)//2
        return query(2*node, start, mid, left, right) * query(2*node+1, mid+1, end, left, right) % DIV
    n, m, k = map(int, input().split())
    tree_size = 2 ** (n.bit_length()+1)
    tree = [1] * (tree_size+1)
    arr = [0]
    for i in range(n):
        arr.append(int(input()))
    tree_init(1, 1, n)
    for i in range(m+k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(1, 1, n, b, c)
            arr[b] = c
        else:
            print(int(query(1, 1, n, b, c)))
solution()