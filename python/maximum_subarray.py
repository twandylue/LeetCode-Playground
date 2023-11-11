class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum: int = nums[0]
        currentSum: int = 0

        for i in range(len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(currentSum, maxSum)

        return maxSum


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
