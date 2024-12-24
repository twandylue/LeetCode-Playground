class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result: int = len(nums)
        for i in range(len(nums)):
            result ^= i ^ nums[i]
        return result


def test_missingNumber_case_1():
    # arrange
    nums: list[int] = [1, 2, 3]
    expected: int = 0

    # act
    actual: int = Solution().missingNumber(nums)

    # assert
    assert actual == expected


def test_missingNumber_case_2():
    # arrange
    nums: list[int] = [0, 2]
    expected: int = 1

    # act
    actual: int = Solution().missingNumber(nums)

    # assert
    assert actual == expected
