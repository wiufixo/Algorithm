import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def solution():
    while True:
        try:
            x = int(input()) * (10**7)
            n = int(input())
            legos = sorted([int(input()) for _ in range(n)])
            ans = []
            l, r = 0, n-1
            flag = False
            while l < r:
                tot = legos[l] + legos[r]
                if tot == x:
                    print(f'yes {legos[l]} {legos[r]}')
                    flag = True
                    break
                if tot < x:
                    l += 1
                else:
                    r -= 1
            if flag:
                continue
            print("danger")
        except:
            break
    
solution()
