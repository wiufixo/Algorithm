word = input()
split = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for s in split:
    if s in word:
        word = word.replace(s, '*')
print(len(word))