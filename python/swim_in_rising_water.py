import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """time complexity: O(n^2 * log n)"""
        n: int = len(grid)
        minHeap: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        visited: set[tuple[int, int]] = set([(0, 0)])
        direction: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while len(minHeap) > 0:
            h, x, y = heapq.heappop(minHeap)
            if x == n - 1 and y == n - 1:
                return h
            for dx, dy in direction:
                nx: int = x + dx
                ny: int = y + dy
                if (
                    nx >= 0
                    and ny >= 0
                    and nx < n
                    and ny < n
                    and (nx, ny) not in visited
                ):
                    heapq.heappush(minHeap, (max(h, grid[ny][nx]), nx, ny))
                    visited.add((nx, ny))

        raise ValueError("Unreachable")


def test_swimInWater_case_1():
    # arrange
    grid: list[list[int]] = [[0, 2], [1, 3]]
    expected: int = 3

    # act
    actual = Solution().swimInWater(grid)

    # assert
    assert actual == expected


def test_swimInWater_case_2():
    # arrange
    grid: list[list[int]] = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    expected: int = 16

    # act
    actual = Solution().swimInWater(grid)

    # assert
    assert actual == expected
