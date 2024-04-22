class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """time complexity: O(n * m), space complexity: O(n * m)"""
        count: int = 0
        visited: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    self.dfs(i, j, visited, grid)
        return count

    def dfs(
        self, i: int, j: int, visited: set[tuple[int, int]], grid: list[list[str]]
    ) -> None:
        if (
            i < 0
            or i >= len(grid)
            or j < 0
            or j >= len(grid[i])
            or grid[i][j] == "0"
            or (i, j) in visited
        ):
            return
        visited.add((i, j))
        self.dfs(i + 1, j, visited, grid)
        self.dfs(i - 1, j, visited, grid)
        self.dfs(i, j + 1, visited, grid)
        self.dfs(i, j - 1, visited, grid)


def test_numIslands_case_1():
    # arrange
    grid: list[list[str]] = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.numIslands(grid)

    # assert
    assert actual == expected


def test_numIslands_case_2():
    # arrange
    grid: list[list[str]] = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.numIslands(grid)

    # assert
    assert actual == expected
