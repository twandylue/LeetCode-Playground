class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        """time complexity: O(n * m), where n is the number of rows and m is the number of columns."""
        result: int = 0
        visited: set[tuple[int, int]] = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) not in visited and grid[r][c] == 0:
                    result += self.dfs(r, c, visited, grid)
        return result

    def dfs(
        self, row: int, col: int, visited: set[tuple[int, int]], grid: list[list[int]]
    ) -> int:
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return 0
        if (row, col) in visited or grid[row][col] == 1:
            return 1
        visited.add((row, col))
        return min(
            self.dfs(row - 1, col, visited, grid),
            self.dfs(row + 1, col, visited, grid),
            self.dfs(row, col - 1, visited, grid),
            self.dfs(row, col + 1, visited, grid),
        )


def test_closedIsland_case_1():
    # arrange
    grid: list[list[int]] = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.closedIsland(grid)

    # assert
    assert expected == actual


def test_closedIsland_case_2():
    # arrange
    grid: list[list[int]] = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.closedIsland(grid)

    # assert
    assert expected == actual


def test_closedIsland_case_3():
    # arrange
    grid: list[list[int]] = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.closedIsland(grid)

    # assert
    assert expected == actual
