class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """time complexity: O(n * m)"""
        result: list[int] = []
        s_row: int = 0
        end_row: int = len(matrix) - 1
        s_col: int = 0
        end_col: int = len(matrix[0]) - 1
        while s_row <= end_row and s_col <= end_col:
            # left -> right
            for i in range(s_col, end_col + 1):
                result.append(matrix[s_row][i])
            s_row += 1
            # up -> down
            for i in range(s_row, end_row + 1):
                result.append(matrix[i][end_col])
            end_col -= 1
            # right -> left (check if row still exists)
            if s_row <= end_row:
                for i in range(end_col, s_col - 1, -1):
                    result.append(matrix[end_row][i])
                end_row -= 1
            # down -> up (check if col still exists)
            if s_col <= end_col:
                for i in range(end_row, s_row - 1, -1):
                    result.append(matrix[i][s_col])
                s_col += 1
        return result


def test_spiralOrder_case_1():
    # arragne
    matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected: list[int] = [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # act
    actual: list[int] = Solution().spiralOrder(matrix)

    # assert
    assert expected == actual


def test_spiralOrder_case_2():
    # arragne
    matrix: list[list[int]] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    expected: list[int] = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # act
    actual: list[int] = Solution().spiralOrder(matrix)

    # assert
    assert expected == actual
