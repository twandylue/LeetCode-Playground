class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """time complexity: O(n * m), space complexity: O(1), where n is the number of rows and m is the number of columns"""
        for r in range(len(board)):
            for c in range(len(board[r])):
                if r == 0 or r == len(board) - 1 or c == 0 or c == len(board[r]) - 1:
                    self.dfs(r, c, board)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

    def dfs(self, r: int, c: int, board: list[list[int]]) -> None:
        if (
            r < 0
            or r == len(board)
            or c < 0
            or c == len(board[r])
            or board[r][c] != "O"
        ):
            return
        board[r][c] = "T"
        self.dfs(r + 1, c, board)
        self.dfs(r - 1, c, board)
        self.dfs(r, c + 1, board)
        self.dfs(r, c - 1, board)


def test_solve_case_1():
    # arrange
    board: list[list[str]] = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    expected: list[list[str]] = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    # act
    solution = Solution()
    solution.solve(board)

    # assert
    assert expected == board


def test_solve_case_2():
    # arrange
    board: list[list[str]] = [
        ["X"],
    ]
    expected: list[list[str]] = [["X"]]

    # act
    solution = Solution()
    solution.solve(board)

    # assert
    assert expected == board
