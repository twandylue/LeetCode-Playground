class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """time complexity: O(n^2), space complexity: O(n^2)"""
        row_set: set[tuple[int, int]] = set()
        col_set: set[tuple[int, int]] = set()
        subbox_set: list[list[set[int]]] = [[set() for _ in range(3)] for _ in range(3)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if not board[row][col].isnumeric():
                    continue
                number: int = int(board[row][col])
                if (row, number) in row_set or (col, number) in col_set:
                    return False
                row_set.add((row, number))
                col_set.add((col, number))
                s_row: int = row // 3
                s_col: int = col // 3
                if number in subbox_set[s_row][s_col]:
                    return False
                subbox_set[s_row][s_col].add(number)
        return True


def test_isValidSudoku_case_1():
    # arrange
    board: list[list[str]] = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isValidSudoku(board)

    # assert
    assert actual == expected


def test_isValidSudoku_case_2():
    # arrange
    board: list[list[str]] = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isValidSudoku(board)

    # assert
    assert actual == expected


def test_isValidSudoku_case_3():
    # arrange
    board: list[list[str]] = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isValidSudoku(board)

    # assert
    assert actual == expected
