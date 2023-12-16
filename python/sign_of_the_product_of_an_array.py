class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product: int = 1
        for num in nums:
            product *= num

        if product > 0:
            return 1
        elif product == 0:
            return 0
        else:
            return -1


def test_arraySign_case_1():
    # arrange
    nums: list[int] = [-1, -2, -3, -4, 3, 2, 1]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.arraySign(nums)

    # assert
    assert expected == actual
