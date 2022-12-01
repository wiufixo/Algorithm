def solution():
    n, c= map(int, input().split())
    data = [int(input()) for _ in range(n)]
    # n, c = 5, 3
    # data = [1,2,8,4,9] # 1 2 4 8 9
    data.sort()
    start = 1
    end = data[-1]-data[0]
    max_min = 0
    while start <= end:
        count = 1
        min_len = 10 ** 10
        mid = (start+end)//2
        k = 0
        for i in range(1, len(data)):
            if data[i]-data[k] >= mid:
                min_len = min(min_len, data[i]-data[k])
                count += 1
                k = i
        if count < c:
            end = mid - 1
        else:
            max_min = max(max_min, min_len)
            start = mid + 1
    print(max_min)
solution()