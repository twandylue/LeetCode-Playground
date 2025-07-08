class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


def test_maxProduct_case_1():
    # arrange
    nums: list[int] = [3, 4, 5, 2]
    expected: int = 12

    # act
    actual = Solution().maxProduct(nums)

    # assert
    assert expected == actual


def test_maxProduct_case_2():
    # arrange
    nums: list[int] = [1, 5, 4, 5]
    expected: int = 16

    # act
    actual = Solution().maxProduct(nums)

    # assert
    assert expected == actual
