import sys
input = sys.stdin.readline
from itertools import combinations

def solution():
    data = input().rstrip()
    stack = []
    groups = []
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(i)
        if data[i] == ')':
            left = stack.pop()
            groups.append((left, i))
    combis = []
    for i in range(1, len(groups)+1):
        for combi in combinations(groups, i):
            combis.append(combi)
    # print(combis)
    ans = []
    for combi in combis:
        word_list = list(data)
        word = ''
        for left, right in combi:
            word_list[left] = word_list[right] = '?'
        for ch in word_list:
            if ch != '?':
                word += ch
        ans.append(word)
    ans.sort()
    check = []
    for a in ans:
        if a not in check:
            print(a)
        check.append(a)
    # for i in range(1, 2 ** len(doubs)):
    #     word = ''
    #     data_list = list(data)
    #     for j in range(len(doubs)):
    #         if i & (1<<j):
    #             # print(doubs[j], end=" ")
    #             for d in doubs[j]:
    #                 data_list[d] = "?"
    #     for ch in data_list:
    #         if ch != "?":
    #             word += ch
    #     ans.append(word)
    # for a in sorted(ans):
    #     print(a)
solution()
