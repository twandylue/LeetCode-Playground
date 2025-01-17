class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """time complexity: O(n)"""
        result: int = nums[0]
        curr_max: int = 0
        for num in nums:
            curr_max = max(curr_max + num, num)
            result = max(result, curr_max)
        return result


def test_maxSubArray_case_1():
    # arrange
    nums: list[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.maxSubArray(nums)

    # assert
    assert actual == expected


def test_maxSubArray_case_2():
    # arrange
    nums: list[int] = [1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.maxSubArray(nums)

    # assert
    assert actual == expected


def test_maxSubArray_case_3():
    # arrange
    nums: list[int] = [5, 4, -1, 7, 8]
    expected: int = 23

    # act
    solution = Solution()
    actual = solution.maxSubArray(nums)

    # assert
    assert actual == expected
