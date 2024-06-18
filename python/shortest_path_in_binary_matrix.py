from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """time complexity: O(n^2), where n is the length of the grid"""
        queue: deque[tuple[int, int, int]] = deque([(0, 0, 1)])
        visited: set[tuple[int, int]] = set()
        visited.add((0, 0))
        dirs: list[list[int]] = [
            [0, 1],
            [0, -1],
            [1, 0],
            [1, 1],
            [1, -1],
            [-1, 0],
            [-1, 1],
            [-1, -1],
        ]
        while len(queue) > 0:
            r, c, length = queue.popleft()
            if min(r, c) < 0 or max(r, c) >= len(grid) or grid[r][c] == 1:
                continue
            if r == len(grid) - 1 and c == len(grid) - 1:
                return length
            for dir_r, dir_c in dirs:
                if (r + dir_r, c + dir_c) not in visited:
                    queue.append((r + dir_r, c + dir_c, length + 1))
                    visited.add((r + dir_r, c + dir_c))
        return -1


def test_shortestPathBinaryMatrix_case_1():
    # arrange
    grid: list[list[int]] = [[0, 1], [1, 0]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.shortestPathBinaryMatrix(grid)

    # assert
    assert expected == actual


def test_shortestPathBinaryMatrix_case_2():
    # arrange
    grid: list[list[int]] = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.shortestPathBinaryMatrix(grid)

    # assert
    assert expected == actual


def test_shortestPathBinaryMatrix_case_3():
    # arrange
    grid: list[list[int]] = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.shortestPathBinaryMatrix(grid)

    # assert
    assert expected == actual
