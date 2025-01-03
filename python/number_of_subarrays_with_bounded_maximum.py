class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        """time complexity: O(n)"""
        return self.count_subarrays_with_max_leq(
            right, nums
        ) - self.count_subarrays_with_max_leq(left - 1, nums)

    def count_subarrays_with_max_leq(self, number: int, nums: list[int]) -> int:
        count: int = 0
        result: int = 0
        for num in nums:
            if num <= number:
                count += 1
            else:
                count = 0
            result += count
        return result


def test_numSubarrayBoundedMax_case_1():
    # arrange
    nums: list[int] = [2, 1, 4, 3]
    left: int = 2
    right: int = 3
    expected: int = 3

    # act
    actual = Solution().numSubarrayBoundedMax(nums, left, right)

    # assert
    assert expected == actual


def test_numSubarrayBoundedMax_case_2():
    # arrange
    nums: list[int] = [2, 9, 2, 5, 6]
    left: int = 2
    right: int = 8
    expected: int = 7

    # act
    actual = Solution().numSubarrayBoundedMax(nums, left, right)

    # assert
    assert expected == actual
