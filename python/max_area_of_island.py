class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """time complexity: O(n*m), space complexity: O(n*m)"""
        result: int = 0
        visited: set[tuple[int, int]] = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) in visited or grid[r][c] == 0:
                    continue
                area: list[int] = [0]
                self.dfs(r, c, area, visited, grid)
                result = max(result, area[0])
        return result

    def dfs(
        self,
        r: int,
        c: int,
        area: list[int],
        visited: set[tuple[int, int]],
        grid: list[list[int]],
    ) -> None:
        if (
            r < 0
            or r == len(grid)
            or c < 0
            or c == len(grid[r])
            or (r, c) in visited
            or grid[r][c] == 0
        ):
            return
        area[0] += 1
        visited.add((r, c))
        self.dfs(r + 1, c, area, visited, grid)
        self.dfs(r - 1, c, area, visited, grid)
        self.dfs(r, c + 1, area, visited, grid)
        self.dfs(r, c - 1, area, visited, grid)


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
