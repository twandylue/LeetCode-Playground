class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """time complexity: O(n * m * 8)"""
        directions: list[tuple[int, int]] = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        for r in range(len(board)):
            for c in range(len(board[r])):
                live_nei: int = 0
                for dc, dr in directions:
                    if (
                        r + dr < 0
                        or r + dr >= len(board)
                        or c + dc < 0
                        or c + dc >= len(board[r])
                        or board[r + dr][c + dc] == 0
                        or board[r + dr][c + dc] == 3
                    ):
                        continue
                    live_nei += 1
                if (live_nei < 2 or live_nei > 3) and board[r][c] == 1:
                    board[r][c] = 2
                elif (live_nei == 2 or live_nei == 3) and board[r][c] == 1:
                    continue
                elif live_nei == 3 and board[r][c] == 0:
                    board[r][c] = 3

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 2:
                    board[r][c] = 0
                if board[r][c] == 3:
                    board[r][c] = 1


def test_gameOfLife_case_1():
    # arrange
    board: list[list[int]] = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    expected: list[list[int]] = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    # act
    Solution().gameOfLife(board)

    # assert
    assert board == expected


def test_gameOfLife_case_2():
    # arrange
    board: list[list[int]] = [[1, 1], [1, 0]]
    expected: list[list[int]] = [[1, 1], [1, 1]]

    # act
    Solution().gameOfLife(board)

    # assert
    assert board == expected
