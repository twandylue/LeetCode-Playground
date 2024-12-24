class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """time complexity: O(n)"""
        result: int = 0
        for num in nums:
            result = result ^ num
        return result


def test_singleNumber_case_1():
    # arrange
    nums: list[int] = [3, 2, 3]
    expected: int = 2

    # act
    actual = Solution().singleNumber(nums)

    # assert
    assert expected == actual


def test_singleNumber_case_2():
    # arrange
    nums: list[int] = [7, 6, 6, 7, 8]
    expected: int = 8

    # act
    actual = Solution().singleNumber(nums)

    # assert
    assert expected == actual
