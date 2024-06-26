import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """time complexity: O(nlogn), space complexity: O(n)"""
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]


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
