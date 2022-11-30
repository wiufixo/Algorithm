def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = 1
        coun = '1'
        ans = []
        def recur(coun, n, k):
            if k >= n:
                res = coun
                coun = coun.replace(" ", "")
                if eval(coun) == 0:
                    ans.append(res)
                return
            k += 1
            recur(coun+'+'+str(k),n,k)
            recur(coun+'-'+str(k),n,k)
            recur(coun+' '+str(k),n,k)
        recur(coun, n, k)
        for answer in sorted(ans):
            print(answer)
        print()
solution()