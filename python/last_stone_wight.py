import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            i = heapq.heappop(heap)
            j = heapq.heappop(heap)
            if j > i:
                remain = i - j
                heapq.heappush(heap, remain)

        return abs(heap[0])


def test_lastStoneWeight_case_1():
    # arrange
    stones: list[int] = [2, 7, 4, 1, 8, 1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.lastStoneWeight(stones)

    # assert
    assert actual == expected


def test_lastStoneWeight_case_2():
    # arrange
    stones: list[int] = [1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.lastStoneWeight(stones)

    # assert
    assert actual == expected
