class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        maxSum: int = nums[0]
        currentMaxSum: int = 0
        minSum: int = nums[0]
        currentMinSum: int = 0
        total: int = 0
        for i in range(len(nums)):
            total += nums[i]
            currentMaxSum = max(nums[i], currentMaxSum + nums[i])
            maxSum = max(currentMaxSum, maxSum)
            currentMinSum = min(nums[i], currentMinSum + nums[i])
            minSum = min(currentMinSum, minSum)

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


def test_maxSubarraySumCircular_case_1():
    # arrange
    nums: list[int] = [1, -2, 3, -2]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.maxSubarraySumCircular(nums)

    # assert
    assert expected == actual


def test_maxSubarraySumCircular_case_2():
    # arrange
    nums: list[int] = [5, -3, 5]
    expected: int = 10

    # act
    solution = Solution()
    actual = solution.maxSubarraySumCircular(nums)

    # assert
    assert expected == actual


def test_maxSubarraySumCircular_case_3():
    # arrange
    nums: list[int] = [-3, -2, -3]
    expected: int = -2

    # act
    solution = Solution()
    actual = solution.maxSubarraySumCircular(nums)

    # assert
    assert expected == actual


def test_maxSubarraySumCircular_case_4():
    # arrange
    nums: list[int] = [-2, -3, -1]
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.maxSubarraySumCircular(nums)

    # assert
    assert expected == actual


def test_maxSubarraySumCircular_case_5():
    # arrange
    nums: list[int] = [-5, 3, 5]
    expected: int = 8

    # act
    solution = Solution()
    actual = solution.maxSubarraySumCircular(nums)

    # assert
    assert expected == actual


def test_maxSubarraySumCircular_case_6():
    # arrange
    nums: list[int] = [1, -6, -7, 4]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.maxSubarraySumCircular(nums)

    # assert
    assert expected == actual
