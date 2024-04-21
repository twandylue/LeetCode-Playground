import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        """
        NOTE:
        1. time complexity: O(klogn), space complexity: O(n)
        2. double heap
        """
        min_heap: list[tuple[int, int]] = list(zip(capital, profits))
        heapq.heapify(min_heap)
        max_heap: list[int] = []
        for _ in range(k):
            while len(min_heap) > 0 and w >= min_heap[0][0]:
                _, pro = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -1 * pro)
            if len(max_heap) == 0:
                break
            w += -1 * heapq.heappop(max_heap)
        return w


def test_findMaximizedCapital_case_1():
    """This is a test case for findMaximizedCapital"""
    # arrange
    k: int = 2
    w: int = 0
    profits: list[int] = [1, 2, 3]
    capital: list[int] = [0, 1, 1]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.findMaximizedCapital(k, w, profits, capital)

    # assert
    assert expected == actual


def test_findMaximizedCapital_case_2():
    """This is a test case for findMaximizedCapital"""
    # arrange
    k: int = 3
    w: int = 0
    profits: list[int] = [1, 2, 3]
    capital: list[int] = [0, 1, 2]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.findMaximizedCapital(k, w, profits, capital)

    # assert
    assert expected == actual


def test_findMaximizedCapital_case_3():
    """This is a test case for findMaximizedCapital"""
    # arrange
    k: int = 1
    w: int = 0
    profits: list[int] = [1, 2, 3]
    capital: list[int] = [0, 1, 2]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.findMaximizedCapital(k, w, profits, capital)

    # assert
    assert expected == actual
