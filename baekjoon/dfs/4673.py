def recur(num, res):
    tot = num
    for i in str(num):
        tot += int(i)
    if tot > 10000:
        return
    res[tot] = False
    recur(tot, res)
res = [True] * (10001)
for num in range(1,10001):
    if res[num]:
        recur(num, res)
for i in range(1, len(res)):
    if res[i]:
        print(i)