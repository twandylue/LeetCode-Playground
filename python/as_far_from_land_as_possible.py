from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        """time complexity: O(n * m), where n is the number of rows and m is the number of columns. space complexity: O(n * m)"""
        result: int = -1
        queue: deque[tuple[int, int]] = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    queue.append((r, c))
        dirs: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(queue) > 0:
            row, col = queue.popleft()
            result = grid[row][col]
            for dir_r, dir_c in dirs:
                next_row: int = row + dir_r
                next_col: int = col + dir_c
                if (
                    min(next_row, next_col) >= 0
                    and max(next_row, next_col) < len(grid)
                    and grid[next_row][next_col] == 0
                ):
                    queue.append((next_row, next_col))
                    grid[next_row][next_col] = grid[row][col] + 1
        return result - 1 if result > 1 else -1


def test_maxDistance_case_1():
    # arrange
    grid: list[list[int]] = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.maxDistance(grid)

    # assert
    assert expected == actual


def test_maxDistance_case_2():
    # arrange
    grid: list[list[int]] = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.maxDistance(grid)

    # assert
    assert expected == actual


def test_maxDistance_case_3():
    # arrange
    grid: list[list[int]] = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.maxDistance(grid)

    # assert
    assert expected == actual


def test_maxDistance_case_4():
    # arrange
    grid: list[list[int]] = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.maxDistance(grid)

    # assert
    assert expected == actual
