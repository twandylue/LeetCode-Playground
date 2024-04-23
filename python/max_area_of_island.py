class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """time complexity: O(n*m), space complexity: O(n*m)"""
        result: int = 0
        visited: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0 and (i, j) not in visited:
                    area: list[int] = [0]
                    self.dfs(i, j, area, visited, grid)
                    result = max(result, area[0])
        return result

    def dfs(
        self,
        i: int,
        j: int,
        area: list[int],
        visited: set[tuple[int, int]],
        grid: list[list[int]],
    ) -> None:
        if (
            i < 0
            or i >= len(grid)
            or j < 0
            or j >= len(grid[i])
            or (i, j) in visited
            or grid[i][j] == 0
        ):
            return
        area[0] += 1
        visited.add((i, j))
        self.dfs(i + 1, j, area, visited, grid)
        self.dfs(i - 1, j, area, visited, grid)
        self.dfs(i, j + 1, area, visited, grid)
        self.dfs(i, j - 1, area, visited, grid)


def test_maxAreaOfIsland_case_1():
    # arrange
    grid: list[list[int]] = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.maxAreaOfIsland(grid)

    # assert
    assert expected == actual


def test_maxAreaOfIsland_case_2():
    # arrange
    grid: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0]]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.maxAreaOfIsland(grid)

    # assert
    assert expected == actual
