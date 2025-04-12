class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """time complexity: O(n * m), space complexity: O(n * m)"""
        result: int = 0
        visited: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in visited or grid[i][j] == "0":
                    continue
                self.dfs(i, j, visited, grid)
                result += 1
        return result

    def dfs(
        self, row: int, col: int, visited: set[tuple[int, int]], grid: [list[list[str]]]
    ) -> None:
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[row])
            or (row, col) in visited
            or grid[row][col] == "0"
        ):
            return
        visited.add((row, col))
        self.dfs(row + 1, col, visited, grid)
        self.dfs(row - 1, col, visited, grid)
        self.dfs(row, col + 1, visited, grid)
        self.dfs(row, col - 1, visited, grid)


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
