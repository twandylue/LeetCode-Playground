from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """time complexity: O(m * n)"""
        visited: set[tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque()
        fresh: list[int] = [0]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh[0] = fresh[0] + 1
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        time: int = 0
        while len(queue) > 0 and fresh[0] > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                self.add_cell(row + 1, col, visited, queue, fresh, grid)
                self.add_cell(row - 1, col, visited, queue, fresh, grid)
                self.add_cell(row, col + 1, visited, queue, fresh, grid)
                self.add_cell(row, col - 1, visited, queue, fresh, grid)
            time += 1
        return time if fresh[0] == 0 else -1

    def add_cell(
        self,
        r: int,
        c: int,
        visited: set[tuple[int, int]],
        queue: deque[tuple[int, int]],
        fresh: list[int],
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
        visited.add((r, c))
        queue.append((r, c))
        grid[r][c] = 2
        fresh[0] -= 1


def test_orangesRotting_case_1():
    # arrange
    grid: list[list[int]] = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.orangesRotting(grid)

    # assert
    assert expected == actual


def test_orangesRotting_case_2():
    # arrange
    grid: list[list[int]] = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.orangesRotting(grid)

    # assert
    assert expected == actual


def test_orangesRotting_case_3():
    # arrange
    grid: list[list[int]] = [[0, 2]]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.orangesRotting(grid)

    # assert
    assert expected == actual
