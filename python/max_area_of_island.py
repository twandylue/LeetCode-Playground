class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxArea: int = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(0, rows):
            for c in range(0, cols):
                area: int = self.walk(c, r, grid)
                maxArea = max(maxArea, area)

        return maxArea

    def walk(self, x: int, y: int, grid: list[list[int]]) -> int:
        area: int = 0

        if x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 0:
            return area
        area += grid[y][x]
        grid[y][x] = 0
        area += self.walk(x + 1, y, grid)
        if x > 0:
            area += self.walk(x - 1, y, grid)

        area += self.walk(x, y + 1, grid)
        if y > 0:
            area += self.walk(x, y - 1, grid)

        return area


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
