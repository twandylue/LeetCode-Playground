class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        """time complexity: O(n * m)"""
        cache: dict[tuple[int, int], int] = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                self.dfs(r, c, cache, -1, matrix)
        return max(cache.values())

    def dfs(
        self,
        row: int,
        col: int,
        cache: dict[tuple[int, int], int],
        prev: int,
        matrix: list[list[int]],
    ) -> int:
        if (
            row < 0
            or row >= len(matrix)
            or col < 0
            or col >= len(matrix[row])
            or matrix[row][col] <= prev
        ):
            return 0
        if (row, col) in cache:
            return cache[(row, col)]
        cache[(row, col)] = max(
            1 + self.dfs(row - 1, col, cache, matrix[row][col], matrix),
            1 + self.dfs(row + 1, col, cache, matrix[row][col], matrix),
            1 + self.dfs(row, col - 1, cache, matrix[row][col], matrix),
            1 + self.dfs(row, col + 1, cache, matrix[row][col], matrix),
        )
        return cache[(row, col)]


def test_longestIncreasingPath_case_1():
    # arrange
    matrix: list[list[int]] = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    expected: int = 4

    # act
    actual = Solution().longestIncreasingPath(matrix)

    # assert
    assert expected == actual


def test_longestIncreasingPath_case_2():
    # arrange
    matrix: list[list[int]] = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    expected: int = 4

    # act
    actual = Solution().longestIncreasingPath(matrix)

    # assert
    assert expected == actual


def test_longestIncreasingPath_case_3():
    # arrange
    matrix: list[list[int]] = [[1]]
    expected: int = 1

    # act
    actual = Solution().longestIncreasingPath(matrix)

    # assert
    assert expected == actual
