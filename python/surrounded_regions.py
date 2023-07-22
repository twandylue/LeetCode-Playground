class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows: int = len(board)
        cols: int = len(board[0])

        for r in range(0, rows):
            for c in range(0, cols):
                if (r == 0 or r == rows - 1) or (c == 0 or c == cols - 1):
                    self.bfs(c, r, board)

        for r in range(0, rows):
            for c in range(0, cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(0, rows):
            for c in range(0, cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

        return

    def bfs(self, x: int, y: int, board: list[list[str]]) -> None:
        if (
            x < 0
            or x >= len(board[0])
            or y < 0
            or y >= len(board)
            or board[y][x] != "O"
        ):
            return

        board[y][x] = "T"
        self.bfs(x + 1, y, board)
        if x > 0:
            self.bfs(x - 1, y, board)

        self.bfs(x, y + 1, board)
        if y > 0:
            self.bfs(x, y - 1, board)
