from collections import deque
def solution():
    n = int(input())
    k = int(input())
    # n = 6
    # k = 3
    # l = 3
    # ds = [['3','D'], ['15','L'], ['17','D']]
    arr = [[0] * n for _ in range(n)]
    arr[0][0] = 2
    # arr[3][4] = arr[2][5] = arr[5][3] = 3
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(k):
        x, y = map(int, input().split())
        arr[x-1][y-1] = 3
    l = int(input())
    ds = [list(input().split()) for _ in range(l)]
    d = 0
    cnt = 0
    x, y = 0, 0 # 머리
    q = deque([(0, 0)])
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] == 2:
            print(cnt+1)
            break
        if arr[nx][ny] == 0: #빈칸일때
            q.append((nx,ny))
            arr[nx][ny] = 2
            # print(q.popleft())
            tail_x, tail_y = q.popleft()
            arr[tail_x][tail_y] = 0
            x, y = nx, ny
        elif arr[nx][ny] == 3: #사과일떄
            q.append((nx,ny))
            arr[nx][ny] = 2
            x, y  = nx, ny
        cnt += 1
        # print(cnt, (x,y))
        for sec, direc in ds:
            if cnt == int(sec):
                # print(cnt, (x,y), d)
                if direc == 'L': # 왼쪽으로 회전
                    d = (d+3) % 4
                else: # 오른쪽으로 회전
                    d = (d+1) % 4
    # print(arr)
solution()
