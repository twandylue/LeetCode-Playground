class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        col_set = set()
        row_set = set()
        sub_cube_set = [set()] * len(board) * len(board[0])

        for r in range(0, len(board)):
            for c in range(0, len(board[r])):
                if not board[r][c].isnumeric():
                    continue

                digit = int(board[r][c], 10)
                if (r, digit) in row_set:
                    return False
                else:
                    row_set.add((r, digit))

                if (c, digit) in col_set:
                    return False
                else:
                    col_set.add((c, digit))

                index = 3 * int(r / 3) + int(c / 3)
                if (index, digit) in sub_cube_set[index]:
                    return False
                else:
                    sub_cube_set[index].add((index, digit))

        return True


def test_isValidSudoku_case1():
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


def test_isValidSudoku_case2():
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
