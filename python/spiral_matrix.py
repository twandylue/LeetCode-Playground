class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """time complexity: O(n * m)"""
        result: list[int] = []
        s_r: int = 0
        e_r: int = len(matrix) - 1
        s_c: int = 0
        e_c: int = len(matrix[0]) - 1
        while s_r <= e_r and s_c <= e_c:
            # left -> right
            for i in range(s_c, e_c + 1):
                result.append(matrix[s_r][i])
            s_r += 1
            # up -> down
            for i in range(s_r, e_r + 1):
                result.append(matrix[i][e_c])
            e_c -= 1
            if s_r <= e_r:
                # right -> left
                for i in range(e_c, s_c - 1, -1):
                    result.append(matrix[e_r][i])
                e_r -= 1
            if s_c <= e_c:
                # down -> up
                for i in range(e_r, s_r - 1, -1):
                    result.append(matrix[i][s_c])
                s_c += 1
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


def test_spiralOrder_case_3():
    # arragne
    matrix: list[list[int]] = [[2, 5, 8], [4, 0, -1]]
    expected: list[int] = [2, 5, 8, -1, 0, 4]

    # act
    actual: list[int] = Solution().spiralOrder(matrix)

    # assert
    assert expected == actual
