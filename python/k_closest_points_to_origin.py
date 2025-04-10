import heapq
from typing import Tuple


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        time complexity: O(nlogn), space complexity: O(n),
        where n is the number of points
        """
        result: list[list[int]] = []
        min_heap: list[tuple[int, int, int]] = []
        for x, y in points:
            distance: int = x**2 + y**2
            heapq.heappush(min_heap, (distance, x, y))
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            result.append([x, y])
        return result


def test_kClosest_case_1():
    # arrange
    points: list[list[int]] = [[1, 3], [-2, 2]]
    k: int = 1
    expected: list[list[int]] = [[-2, 2]]

    # act
    solution = Solution()
    actual = solution.kClosest(points, k)

    # assert
    assert actual == expected


def test_kClosest_case_2():
    # arrange
    points: list[list[int]] = [[3, 3], [5, -1], [-2, 4]]
    k: int = 2
    expected: list[list[int]] = [[3, 3], [-2, 4]]

    # act
    solution = Solution()
    actual = solution.kClosest(points, k)

    # assert
    assert actual == expected
