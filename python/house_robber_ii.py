class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.robHelper(nums[1:]), self.robHelper(nums[:-1]))

    def robHelper(self, nums: list[int]) -> int:
        rob1: int = 0
        rob2: int = 0
        for n in nums:
            newRob: int = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2


def test_rob_case_1():
    # arrange
    nums: list[int] = [2, 3, 2]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.rob(nums)

    # assert
    assert expected == actual


def test_rob_case_2():
    # arrange
    nums: list[int] = [1, 2, 3, 1]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.rob(nums)

    # assert
    assert expected == actual


def test_rob_case_3():
    # arrange
    nums: list[int] = [1, 2, 3]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.rob(nums)

    # assert
    assert expected == actual
