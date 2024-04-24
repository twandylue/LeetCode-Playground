class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """time complexity: O(n * m), space complexity: O(n * m)"""
        visited: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    return self.dfs(i, j, visited, grid)
        return 0

    def dfs(
        self, i: int, j: int, visited: set[tuple[int, int]], grid: list[list[int]]
    ) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        return (
            self.dfs(i + 1, j, visited, grid)
            + self.dfs(i - 1, j, visited, grid)
            + self.dfs(i, j + 1, visited, grid)
            + self.dfs(i, j - 1, visited, grid)
        )


def test_islandPerimeter_case_1():
    """This is a test case for islandPerimeter"""
    # arrange
    grid: list[list[int]] = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    expected: int = 16

    # act
    solution = Solution()
    actual = solution.islandPerimeter(grid)

    # assert
    assert expected == actual


def test_islandPerimeter_case_2():
    """This is a test case for islandPerimeter"""
    # arrange
    grid: list[list[int]] = [[1]]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.islandPerimeter(grid)

    # assert
    assert expected == actual
