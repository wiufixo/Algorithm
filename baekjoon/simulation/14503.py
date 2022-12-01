def solution():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    arr[r][c] = 2
    cnt = 1
    while True:
        flag = False
        for i in range(4):
            d = (d + 3)%4
            nx = r + dx[d]
            ny = c + dy[d]
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                cnt += 1
                flag = True
                r = nx
                c = ny
                break
        if not flag: 
            nd = (d + 2) % 4
            nx = r + dx[nd]
            ny = c + dy[nd]
            if arr[nx][ny] == 1:
                print(cnt)
                break
            r = nx
            c = ny
solution()
