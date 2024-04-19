class TrieNode:
    def __init__(self):
        self._char_map: dict[str, TrieNode] = {}
        self._is_terminal: bool = False

    def insert(self, word: str, idx: int) -> None:
        """time complexity: O(n). n is the length of the word."""
        if idx >= len(word):
            self._is_terminal = True
            return
        if word[idx] not in self._char_map:
            self._char_map[word[idx]] = TrieNode()
        self._char_map[word[idx]].insert(word, idx + 1)

    def search(self, word: str, idx: int) -> bool:
        """time complexity: O(n). n is the length of the word."""
        if idx >= len(word):
            return self._is_terminal
        if word[idx] not in self._char_map:
            return False
        return self._char_map[word[idx]].search(word, idx + 1)

    def startsWith(self, prefix: str, idx: int) -> bool:
        """time complexity: O(n). n is the length of the prefix."""
        if idx >= len(prefix):
            return True
        if prefix[idx] not in self._char_map:
            return False
        return self._char_map[prefix[idx]].startsWith(prefix, idx + 1)


class Trie:
    """This is a Trie class."""

    def __init__(self):
        self._root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        self._root.insert(word, 0)

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        return self._root.search(word, 0)

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        return self._root.startsWith(prefix, 0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
def test_trie_case_1():
    """This is a test case for Trie."""
    trie: Trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")  # return True
    assert not trie.search("app")  # return False
    assert trie.startsWith("app")  # return True
    trie.insert("app")
    assert trie.search("app")  # return True


def test_trie_case_2():
    """This is a test case for Trie."""
    trie: Trie = Trie()
    trie.insert("a")
    assert trie.search("a")  # return True
    assert trie.startsWith("a")  # return True
