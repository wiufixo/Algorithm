import sys
input = sys.stdin.readline
min_papers = 30
def solution():
    def check(i,j,k,num):
        flag = True
        for a in range(i, i+k):
            for b in range(j, j+k):
                if g[a][b] != num:
                    flag = False
        return flag
    def cover(i,j,k,num):
        for a in range(i, i+k):
            for b in range(j, j+k):
                g[a][b] = num
    def dfs(pos):
        global min_papers
        if pos == 100 :
            # print(papers)
            min_papers = min(min_papers, sum(papers))
            return
        row = pos // 10
        col = pos % 10
        
        if g[row][col] == 1:
            for k in range(1,6):
                if papers[k] == 5:
                    continue
                if row + k <= 10 and col + k <= 10:
                    if check(row, col, k, 1):
                        cover(row, col, k, 0)
                        papers[k] += 1
                        dfs(pos+k)
                        papers[k] -= 1
                        cover(row, col, k, 1)
        else:
            dfs(pos+1)
    
    papers = [0,0,0,0,0,0]
    g = [list(map(int, input().split())) for _ in range(10)]
    # g = [
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [0,1,1,0,0,0,0,0,0,0],
    #     [0,0,1,0,0,0,0,0,0,0],
    #     [0,0,0,0,1,1,0,0,0,0],
    #     [0,0,0,0,1,1,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [0,0,1,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0],
    # ]
    dfs(0)
    print(min_papers if min_papers != 30 else -1)

solution()