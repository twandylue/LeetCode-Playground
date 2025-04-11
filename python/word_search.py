class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited: set[tuple[int, int]] = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(0, i, j, visited, board, word):
                    return True
        return False

    def dfs(
        self,
        i: int,
        row: int,
        col: int,
        visited: set[tuple[int, int]],
        board: list[list[str]],
        word: str,
    ) -> bool:
        if i == len(word):
            return True
        if (
            row < 0
            or row >= len(board)
            or col < 0
            or col >= len(board[row])
            or (row, col) in visited
            or board[row][col] != word[i]
        ):
            return False
        visited.add((row, col))
        result: bool = (
            self.dfs(i + 1, row + 1, col, visited, board, word)
            or self.dfs(i + 1, row - 1, col, visited, board, word)
            or self.dfs(i + 1, row, col + 1, visited, board, word)
            or self.dfs(i + 1, row, col - 1, visited, board, word)
        )
        visited.remove((row, col))
        return result


def test_exist_case_1():
    # Arrange
    board: list[list[str]] = [
        ["A", "B", "C", "D"],
        ["S", "A", "A", "T"],
        ["A", "C", "A", "E"],
    ]
    word = "CAT"
    expected: bool = True

    # Act
    result: bool = Solution().exist(board, word)

    # Assert
    assert result == expected


def test_exist_case_2():
    # Arrange
    board: list[list[str]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "SEE"
    expected: bool = True

    # Act
    result: bool = Solution().exist(board, word)

    # Assert
    assert result == expected


def test_exist_case_3():
    # Arrange
    board: list[list[str]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word = "ABCD"
    expected: bool = False

    # Act
    result: bool = Solution().exist(board, word)

    # Assert
    assert result == expected
