def solution():
    arr = set()
    def plus(pos, cnt):
        if check():
            arr.add(cnt)
            # print(cnt, g)
            return 
        if cnt == 3 or pos >= r*c:
            return
        row = pos // c
        col = pos % c
        if col < c-1 and g[row][col] == 0 and g[row][col+1] == 0:
            g[row][col], g[row][col+1] = 1, 2
            plus(pos+2, cnt+1)
            g[row][col], g[row][col+1] = 0, 0
        plus(pos+1, cnt)
    def check():
        for i in range(c):
            col = i
            row = 0
            while row < r:
                if g[row][col] == 1:
                    col += 1
                elif g[row][col] == 2:
                    col -= 1
                row += 1
            if col != i:
                return False
        return True
        # print(g)
        # if cnt > 3:
        #     return False
        # print("c",c)
        # for i in range(c):
        #     col = i
        #     start = 0
        #     for j in range(start, r):
        #         if g[j][col] == 1:
        #             col += 1
        #             start = j+1
        #             continue
        #         if g[j][col] == 2:
        #             col -= 1
        #             start = j+1
        #             continue
        #         while g[j][col] == 0 and j < r-1:
        #             j += 1
        #         start = j
        #     print("i",i, col)
        #     if i != col:
        #         return False
            
        # return True
        pass
    def dfs(i,j, cnt):
        pass
        
    c, k, r = map(int, input().split())
    g = [[0] * (c) for _ in range(r)]
    for i in range(k):
        x, y = map(int, input().split())
        g[x-1][y-1], g[x-1][y] = 1, 2
        
    plus(0, 0)
    # print(arr)
    if not arr:
        print(-1)
    else:
        print(min(arr))
solution()
