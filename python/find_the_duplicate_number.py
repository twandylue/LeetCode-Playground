class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d: dict[int, int] = dict()
        for n in nums:
            if n in d:
                return n
            d[n] = 1
        return 0


def test_findDuplicate_case_1():
    # arrange
    nums: list[int] = [1, 3, 4, 2, 2]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.findDuplicate(nums)

    # assert
    assert expected == actual


def test_findDuplicate_case_2():
    # arrange
    nums: list[int] = [3, 1, 3, 4, 2]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.findDuplicate(nums)

    # assert
    assert expected == actual
