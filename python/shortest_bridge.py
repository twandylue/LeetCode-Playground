from collections import deque


class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        """time complexity: O(n^2), where n is the length of the grid"""
        visited: set[tuple[int, int]] = set()
        dirs: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    self.dfs(r, c, grid, dirs, visited)
                    return self.bfs(grid, dirs, visited)
        return -1

    def dfs(
        self,
        row: int,
        col: int,
        grid: list[list[int, int]],
        dirs: list[tuple[int, int]],
        visited: set[tuple[int, int]],
    ):
        if (
            min(row, col) < 0
            or max(row, col) >= len(grid)
            or grid[row][col] == 0
            or (row, col) in visited
        ):
            return
        visited.add((row, col))
        for dir_r, dir_c in dirs:
            self.dfs(row + dir_r, col + dir_c, grid, dirs, visited)

    def bfs(
        self,
        grid: list[list[int, int]],
        dirs: list[tuple[int, int]],
        visited: set[tuple[int, int]],
    ) -> int:
        queue: deque[tuple[int, int]] = deque(visited)
        result: int = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dir_r, dir_c in dirs:
                    next_r: int = row + dir_r
                    next_c: int = col + dir_c
                    if (
                        min(next_r, next_c) < 0
                        or max(next_r, next_c) >= len(grid)
                        or (next_r, next_c) in visited
                    ):
                        continue
                    if grid[next_r][next_c] == 1:
                        return result
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))
            result += 1
        return -1


def test_shortestBridge_case_1():
    # arrange
    grid: list[list[int]] = [[0, 1], [1, 0]]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.shortestBridge(grid)

    # assert
    assert expected == actual


def test_shortestBridge_case_2():
    # arrange
    grid: list[list[int]] = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.shortestBridge(grid)

    # assert
    assert expected == actual


def test_shortestBridge_case_3():
    # arrange
    grid: list[list[int]] = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.shortestBridge(grid)

    # assert
    assert expected == actual
