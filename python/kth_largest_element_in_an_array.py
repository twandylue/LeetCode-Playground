import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """time complexity: O(klon(n)) where n is the length of nums, and k is the kth largest element"""
        min_heap: list[int] = nums
        heapq.heapify(min_heap)
        for _ in range(len(min_heap) - k):
            heapq.heappop(min_heap)
        return min_heap[0]


def test_kClosest_case_1():
    # arrange
    nums: list[int] = [3, 2, 1, 5, 6, 4]
    k: int = 2
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.findKthLargest(nums, k)

    # assert
    assert expected == actual


def test_kClosest_case_2():
    # arrange
    nums: list[int] = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k: int = 4
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.findKthLargest(nums, k)

    # assert
    assert expected == actual


def test_kClosest_case_3():
    # arrange
    nums: list[int] = [5, 2, 4, 1, 3, 6, 0]
    k: int = 4
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.findKthLargest(nums, k)

    # assert
    assert expected == actual
