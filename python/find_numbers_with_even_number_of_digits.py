class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        result: int = 0
        for num in nums:
            count: int = len(str(num))
            if count % 2 == 0:
                result += 1
        return result


def test_findNumbers_case_1():
    # arrange
    nums: list[int] = [12, 345, 2, 6, 7896]
    expected: int = 2

    # act
    actual: int = Solution().findNumbers(nums)

    # assert
    assert expected == actual


def test_findNumbers_case_2():
    # arrange
    nums: list[int] = [555, 901, 482, 1771]
    expected: int = 1

    # act
    actual: int = Solution().findNumbers(nums)

    # assert
    assert expected == actual
