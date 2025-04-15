class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        """time complexity: O(n^2), space complexity: O(n^2)"""
        result: list[int] = [[1 for _ in range(n)] for _ in range(n)]
        s_row: int = 0
        e_row: int = len(result) - 1
        s_col: int = 0
        e_col: int = len(result[0]) - 1
        curr_value: int = 1
        while s_row <= e_row and s_col <= e_col:
            # left -> right
            for i in range(s_col, e_col + 1):
                result[s_row][i] = curr_value
                curr_value += 1
            s_row += 1
            # up -> down
            for i in range(s_row, e_row + 1):
                result[i][e_col] = curr_value
                curr_value += 1
            e_col -= 1
            # right -> left
            if s_row <= e_row:
                for i in range(e_col, s_col - 1, -1):
                    result[e_row][i] = curr_value
                    curr_value += 1
                e_row -= 1
            # down -> up
            if s_col <= e_col:
                for i in range(e_row, s_row - 1, -1):
                    print(f"row: {i}, col: {s_col}")
                    print(result)
                    result[i][s_col] = curr_value
                    curr_value += 1
                s_col += 1
        return result


def test_generateMatrix_case_1():
    # arragne
    n: int = 3
    expected: list[list[int]] = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    # act
    actual: list[int] = Solution().generateMatrix(n)

    # assert
    assert expected == actual


def test_generateMatrix_case_2():
    # arragne
    n: int = 1
    expected: list[list[int]] = [[1]]

    # act
    actual: list[int] = Solution().generateMatrix(n)

    # assert
    assert expected == actual
