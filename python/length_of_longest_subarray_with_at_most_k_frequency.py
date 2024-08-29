from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        """time complexity: O(n)"""
        l: int = 0
        result: int = 0
        count: dict[int, int] = defaultdict(int)
        for r in range(len(nums)):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result


def test_maxSubarrayLength_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 1, 2, 3, 1, 2]
    k: int = 2
    expected: int = 6

    # act
    actual = Solution().maxSubarrayLength(nums, k)

    # assert
    assert expected == actual


def test_maxSubarrayLength_case_2():
    # arrange
    nums: list[int] = [1, 2, 1, 2, 1, 2, 1, 2]
    k: int = 1
    expected: int = 2

    # act
    actual = Solution().maxSubarrayLength(nums, k)

    # assert
    assert expected == actual


def test_maxSubarrayLength_case_3():
    # arrange
    nums: list[int] = [5, 5, 5, 5, 5, 5, 5]
    k: int = 4
    expected: int = 4

    # act
    actual = Solution().maxSubarrayLength(nums, k)

    # assert
    assert expected == actual
