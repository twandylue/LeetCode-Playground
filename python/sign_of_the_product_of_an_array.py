class Solution:
    def arraySign(self, nums: list[int]) -> int:
        negative: int = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 1:
                negative += 1

        if negative % 2 == 0:
            return 1
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
