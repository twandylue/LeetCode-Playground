class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """time complexity: O(n)"""
        goal: int = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


def test_canJump_case_1():
    # arrange
    expected: bool = True
    nums: list[int] = [2, 3, 1, 1, 4]

    # act
    actual: bool = Solution().canJump(nums)

    # assert
    assert expected == actual


def test_canJump_case_2():
    # arrange
    nums: list[int] = [3, 2, 1, 0, 4]
    expected: bool = False

    # act
    actual: bool = Solution().canJump(nums)

    # assert
    assert expected == actual
