from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        time: int = 0
        fresh: int = 0
        queue: deque[tuple[int, int]] = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        dirs: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(queue) > 0 and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    row: int = r + dr
                    col: int = c + dc
                    if (
                        row < 0
                        or row >= len(grid)
                        or col < 0
                        or col >= len(grid[row])
                        or grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    queue.append((row, col))
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
