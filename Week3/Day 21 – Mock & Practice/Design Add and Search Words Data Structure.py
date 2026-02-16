class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur=cur.children[char]
        cur.word=True

    def search(self, word: str) -> bool:
        def dfs(cur,i):
            if i==len(word):
                return cur.word

            if word[i]=='.':
                next_nodes=cur.children.values()
            else:
                if word[i] not in cur.children:
                    return False
                next_nodes=[cur.children[word[i]]]

            for child in next_nodes:
                if dfs(child,i+1):
                    return True
            return False

        return dfs(self.root,0)

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("pad"))
#TC: addWord: O(n) , search: O(t)
#Sc: addWord: O(n), search: O(n)  Total: O(t + n)
# n = length of the string and
# t = total number of TrieNodes created in the Trie.




