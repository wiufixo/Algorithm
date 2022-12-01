from collections import deque
def solution():
    def move(x, y, dx, dy):
        cnt = 0
        while g[x+dx][y+dy] != '#' and g[x][y] != 'O':
            x += dx
            y += dy
            cnt += 1
        return x, y, cnt
    def bfs(rx, ry, bx, by):
        visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
        # print(visited)
        visited[rx][ry][bx][by] = True
        q = deque([[rx, ry, bx, by, 0]])
        while q:
            a_, b_, c_, d_, tot  = q.popleft()
            # print("q",a_, b_, c_, d_, tot)
            
            # if visited[a][b][c][d]:
            #     continue
            if tot >= 10:
                print(-1)
                return
            for i in range(4):
                a, b, acnt = move(a_, b_, dx[i], dy[i])
                c, d, ccnt = move(c_, d_, dx[i], dy[i])
                if g[c][d] == 'O':
                    continue
                if g[a][b] == 'O':
                    print(tot+1)
                    return
                if a == c and b == d: # 둘이 겹쳐지는 기울임
                    if acnt > ccnt:
                        a, b = a-dx[i], b-dy[i]
                    else:
                        c, d = c-dx[i], d-dy[i]
                # print("red", a,b,acnt,tot,"i",i)
                # print("blue", c,d,ccnt,tot,"i",i)
                
                # if a == a_ and b == b_ and c == c_ and d == d_:
                #     # print("안움직임")
                #     continue
                
                if visited[a][b][c][d]:
                    # print("방문함")
                    continue
                visited[a][b][c][d] = True
                q.append([a,b,c,d,tot+1])
                # print(a,b,c,d,tot+1)
                # print("----------")
                # return
        print(-1)

                    
    # n, m = 7,7
    # g = [
    #     ['#','#','#','#','#','#','#'], 
    #     ['#','.','.','.','R','B','#'],
    #     ['#','.','#','#','#','#','#'],
    #     ['#','.','.','.','.','.','#'],
    #     ['#','#','#','#','#','.','#'],
    #     ['#','O','.','.','.','.','#'],
    #     ['#','#','#','#','#','#','#']
    # ]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    red = []
    blue = []
    hole = []
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'R':
                red.append(i)
                red.append(j)
            if g[i][j] == 'B':
                blue.append(i)
                blue.append(j)
            if g[i][j] == 'O':
                hole.append(i)
                hole.append(j)
    bfs(red[0], red[1], blue[0], blue[1])
solution()




