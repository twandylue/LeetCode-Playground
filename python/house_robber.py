class Solution:
    def rob(self, nums: list[int]) -> int:
        """time complexity: O(n)"""
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp: list[int] = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


def test_rob_case_1():
    # arragne
    nums: list[int] = [1, 2, 3, 1]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.rob(nums)

    # assert
    assert expected, actual


def test_rob_case_2():
    # arragne
    nums: list[int] = [2, 7, 9, 3, 1]
    expected: int = 12

    # act
    solution = Solution()
    actual = solution.rob(nums)

    # assert
    assert expected, actual
