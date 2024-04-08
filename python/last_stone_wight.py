import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """time complexity: O(nlogn), space complexity: O(n)"""
        min_heap: list[int] = [-s for s in stones]
        heapq.heapify(min_heap)
        while len(min_heap) > 1:
            f: int = heapq.heappop(min_heap)
            s: int = heapq.heappop(min_heap)
            heapq.heappush(min_heap, f - s)
        return abs(min_heap[0])


def test_lastStoneWeight_case_1():
    """This is a test case for lastStoneWeight"""
    # arrange
    stones: list[int] = [2, 7, 4, 1, 8, 1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.lastStoneWeight(stones)

    # assert
    assert actual == expected


def test_lastStoneWeight_case_2():
    """This is a test case for lastStoneWeight"""
    # arrange
    stones: list[int] = [1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.lastStoneWeight(stones)

    # assert
    assert actual == expected
