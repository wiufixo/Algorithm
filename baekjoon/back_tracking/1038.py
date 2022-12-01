count = 9
def solution():
    def make_num(limit, num):
        global count
        if len(num) == limit:
            count += 1
            if count == n:
                print(int(num))
                exit(0)
            return
        if len(num) == 0:
            for i in range(limit-1,10):
                make_num(limit, num+str(i))
        else:
            for i in range(0,int(num[-1])):
                if int(num[-1]) > i:
                    make_num(limit, num+str(i))
    n = int(input())
    if n > 1022:
        print(-1)
        return
    if n < 10:
        print(n)
        return
    for i in range(2,11):
        make_num(i, '')
solution()
