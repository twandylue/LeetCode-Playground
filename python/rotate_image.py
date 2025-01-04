class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """time complexity: O(m * n)"""
        COLS: int = len(matrix[0])
        for r in range(len(matrix)):
            for c in range(r, len(matrix[r])):
                tmp: int = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp

        for r in range(len(matrix)):
            for c in range(len(matrix[r]) // 2):
                tmp: int = matrix[r][c]
                matrix[r][c] = matrix[r][COLS - 1 - c]
                matrix[r][COLS - 1 - c] = tmp


def test_rotate_case_1():
    # arrange
    matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected: list[list[int]] = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # act
    Solution().rotate(matrix)

    # assert
    assert matrix == expected


def test_rotate_case_2():
    # arrange
    matrix: list[list[int]] = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
    ]
    expected: list[list[int]] = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
    ]

    # act
    Solution().rotate(matrix)

    # assert
    assert matrix == expected
