class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        """time complexity: O(n * m), where n is the number of rows and m is the number of columns.
        space complexity: O(n * m)"""
        visited: set[tuple[int, int]] = set()
        dirs: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        border_lands: int = 0
        total_lands: int = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                total_lands += grid[r][c]
                if (
                    (r, c) not in visited
                    and (r in [0, len(grid) - 1] or c in [0, len(grid[r]) - 1])
                    and grid[r][c] == 1
                ):
                    border_lands += self.dfs(r, c, dirs, visited, grid)
        return total_lands - border_lands

    def dfs(
        self,
        row: int,
        col: int,
        dirs: list[tuple[int, int]],
        visited: set[tuple[int, int]],
        grid: list[list[int]],
    ) -> int:
        if (
            row < 0
            or col < 0
            or row >= len(grid)
            or col >= len(grid[0])
            or (row, col) in visited
            or grid[row][col] == 0
        ):
            return 0
        result = 1
        visited.add((row, col))
        for dir_r, dir_c in dirs:
            result += self.dfs(row + dir_r, col + dir_c, dirs, visited, grid)
        return result


def test_numEnclaves_case_1():
    # arrange
    grid: list[list[int]] = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.numEnclaves(grid)

    # assert
    assert expected == actual


def test_numEnclaves_case_2():
    # arrange
    grid: list[list[int]] = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.numEnclaves(grid)

    # assert
    assert expected == actual
