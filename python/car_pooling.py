import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """complexity: O(nlogn), space complexity: O(n)"""
        trips = sorted(trips, key=lambda x: x[1])
        min_heap: list[tuple[int, int]] = []
        accu: int = 0
        for trip in trips:
            while len(min_heap) > 0 and trip[1] >= min_heap[0][0]:
                _, remove = heapq.heappop(min_heap)
                accu -= remove
            accu += trip[0]
            heapq.heappush(min_heap, (trip[2], trip[0]))
            if accu > capacity:
                return False
        return True


def test_carPooling_case_1():
    # arrange
    trips: list[list[int]] = [[2, 1, 5], [3, 3, 7]]
    capacity: int = 4
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.carPooling(trips, capacity)

    # assert
    assert expected == actual


def test_carPooling_case_2():
    # arrange
    trips: list[list[int]] = [[2, 1, 5], [3, 3, 7]]
    capacity: int = 5
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.carPooling(trips, capacity)

    # assert
    assert expected == actual


def test_carPooling_case_3():
    # arrange
    trips: list[list[int]] = [[2, 1, 5], [3, 5, 7]]
    capacity: int = 3
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.carPooling(trips, capacity)

    # assert
    assert expected == actual


def test_carPooling_case_4():
    # arrange
    trips: list[list[int]] = [[8, 2, 3], [4, 1, 3], [1, 3, 6], [8, 4, 6], [4, 4, 8]]
    capacity: int = 12
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.carPooling(trips, capacity)

    # assert
    assert expected == actual
