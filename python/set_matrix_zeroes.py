class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols: list[int] = []
        rows: list[int] = []
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[r])):
                if matrix[r][c] == 0:
                    cols.append(c)
                    rows.append(r)

        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[r])):
                if r in rows or c in cols:
                    matrix[r][c] = 0


def test_setZeroes_case_1():
    # Arrange
    maxtrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    # Act
    Solution().setZeroes(maxtrix)

    # Assert
    assert maxtrix == expected


def test_setZeroes_case_2():
    # Arrange
    maxtrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    # Act
    Solution().setZeroes(maxtrix)

    # Assert
    assert maxtrix == expected
