class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target: int = sum(nums) // 2
        dp: set[int] = set()
        dp.add(0)

        for n in nums:
            nextDP = dp.copy()
            for i in dp:
                nextDP.add(i + n)
            dp = nextDP

        return True if target in dp else False


def test_canPartition_test_1():
    # arrange
    nums: list[int] = [1, 5, 11, 5]
    expected: bool = True

    # act
    solution = Solution()
    actual: bool = solution.canPartition(nums)

    # assert
    assert actual == expected


def test_canPartition_test_2():
    # arrange
    nums: list[int] = [1, 2, 3, 5]
    expected: bool = False

    # act
    solution = Solution()
    actual: bool = solution.canPartition(nums)

    # assert
    assert actual == expected
