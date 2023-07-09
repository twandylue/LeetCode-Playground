import heapq
from typing import Tuple


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points:
            distance: int = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (distance, point))

        result: list[Tuple[int, list[int]]] = heapq.nsmallest(k, heap)

        # return [x[1] for x in result]
        return list(map(lambda x: x[1], result))


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
