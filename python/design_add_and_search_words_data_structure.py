class TrieNode:
    def __init__(self):
        self.child: dict[str, TrieNode] = {}
        self.is_word: bool = False


class WordDictionary:

    def __init__(self):
        self._root = TrieNode()

    def addWord(self, word: str) -> None:
        """time complexity: O(n)"""
        curr: TrieNode = self._root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        """time complexity: O(n)"""
        return self._dfs(0, self._root, word)

    def _dfs(self, i: int, root: TrieNode, word: str) -> bool:
        curr: TrieNode = root
        for x in range(i, len(word)):
            c: str = word[x]
            if c == ".":
                for child in curr.child.values():
                    if self._dfs(x + 1, child, word):
                        return True
                return False
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.is_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
def test_worddictionary_case1():
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    dictionary = WordDictionary()
    dictionary.addWord("bad")
    dictionary.addWord("dad")
    dictionary.addWord("mad")
    assert dictionary.search("bad") == True
    assert dictionary.search(".ad") == True
    assert dictionary.search("b..") == True
