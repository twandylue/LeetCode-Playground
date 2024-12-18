class TrieNode:
    def __init__(self):
        self.child: dict[str, TrieNode] = {}
        self.is_word: bool = False

    def add_word(self, word: str) -> None:
        curr: TrieNode = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.is_word = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """time complexity: O(m * n * 4 * 3^(t-1) + s) Where
        m is the number of rows,
        n is the number of columns,
        t is the maximum length of any word in the array words
        and s is the sum of the lengths of all the words."""
        root: TrieNode = TrieNode()
        for word in words:
            root.add_word(word)
        result: set[str] = set()
        visited: set[tuple[int, int]] = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                self.dfs(r, c, root, visited, result, board, "")

        return list(result)

    def dfs(
        self,
        row: int,
        col: int,
        node: TrieNode,
        visited: set[tuple[int, int]],
        result: set[str],
        board: list[list[str]],
        word: str,
    ) -> None:
        if (
            row < 0
            or row >= len(board)
            or col < 0
            or col >= len(board[row])
            or (row, col) in visited
            or board[row][col] not in node.child
        ):
            return
        node = node.child[board[row][col]]
        visited.add((row, col))
        word += board[row][col]
        if node.is_word:
            result.add(word)
        self.dfs(row - 1, col, node, visited, result, board, word)
        self.dfs(row + 1, col, node, visited, result, board, word)
        self.dfs(row, col - 1, node, visited, result, board, word)
        self.dfs(row, col + 1, node, visited, result, board, word)
        visited.remove((row, col))


def test_findWords_case_1():
    # arrange
    board: list[list[str]] = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words: list[str] = ["oath", "pea", "eat", "rain"]
    expected: list[str] = ["eat", "oath"]
    expected.sort()

    # act
    actual: list[str] = Solution().findWords(board, words)

    # assert
    assert expected == actual
