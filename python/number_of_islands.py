class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count: int = 0
        h: int = len(grid)
        w: int = len(grid[0])
        for row in range(0, h):
            for col in range(0, w):
                if grid[row][col] == "1":
                    count += 1
                    self.walk(col, row, grid)

        return count

    def walk(self, x: int, y: int, grid: list[list[str]]) -> None:
        if y >= len(grid) or x >= len(grid[0]) or grid[y][x] == "0":
            return

        grid[y][x] = "0"
        self.walk(x + 1, y, grid)
        if x > 0:
            self.walk(x - 1, y, grid)

        self.walk(x, y + 1, grid)
        if y > 0:
            self.walk(x, y - 1, grid)

        return None


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
