n = int(input())
words = [input() for i in range(n)]
cnt = n
for word in words:
    alpha = {}
    for i in range(len(word)):
        if i>0 and word[i] != word[i-1] and word[i] in alpha:
            cnt -= 1
            break
        if word[i] not in alpha:
            alpha[word[i]] = 0
        alpha[word[i]] += 1
print(cnt)