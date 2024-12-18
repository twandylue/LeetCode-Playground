from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        """time complexity: O(m * n)"""
        visited: set[tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        dist: int = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = dist
                self.add_cell(row - 1, col, visited, queue, grid)
                self.add_cell(row + 1, col, visited, queue, grid)
                self.add_cell(row, col - 1, visited, queue, grid)
                self.add_cell(row, col + 1, visited, queue, grid)
            dist += 1

    def add_cell(
        self,
        row: int,
        col: int,
        visited: set[tuple[int, int]],
        queue: deque[tuple[int, int]],
        grid: list[list[int]],
    ) -> None:
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[row])
            or (row, col) in visited
            or grid[row][col] == -1
        ):
            return
        visited.add((row, col))
        queue.append((row, col))


def test_islandsAndTreasure_case_1():
    # arrange
    grid: list[list[int]] = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    expected: list[list[int]] = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]

    # act
    Solution().islandsAndTreasure(grid)

    # assert
    assert expected == grid


def test_islandsAndTreasure_case_2():
    # arrange
    grid: list[list[int]] = [[0, -1], [2147483647, 2147483647]]
    expected: list[list[int]] = [[0, -1], [1, 2]]

    # act
    Solution().islandsAndTreasure(grid)

    # assert
    assert expected == grid
