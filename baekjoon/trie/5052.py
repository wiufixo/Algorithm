import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.child = {}
class Trie:
    def __init__(self):
        self.head = Node(None)
    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.data = word
    def search(self, prefix):
        cur = self.head
        for ch in prefix:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        if cur.child:
            return True
        return False
def solution():
    t = int(input().rstrip())
    for _ in range(t):
        n = int(input().rstrip())
        words = []
        for _ in range(n):
            words.append(input().rstrip())
        data = Trie()
        for word in words:
            data.add(word)
        ans = "YES"
        for word in words:
            if data.search(word):
                # print("NO")
                ans = "NO"
                break
        # if flag:
        #     continue
        print(ans)
solution()
