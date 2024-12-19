from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """time complexity: O(m * n)"""
        time: int = 0
        fresh: int = 0
        visited: set[tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(queue) > 0 and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r: int = row + dr
                    c: int = col + dc
                    if (
                        r < 0
                        or r >= len(grid)
                        or c < 0
                        or c >= len(grid[r])
                        or (r, c) in visited
                        or grid[r][c] == 0
                    ):
                        continue
                    visited.add((r, c))
                    queue.append((r, c))
                    grid[r][c] = 2
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


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
