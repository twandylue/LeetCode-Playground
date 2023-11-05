class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsSet: set[int] = set(nums)
        if len(numsSet) == len(nums):
            return False
        return True


def test_containsDuplicate_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 1]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.containsDuplicate(nums)

    # assert
    assert expected == actual


def test_containsDuplicate_case_2():
    # arrange
    nums: list[int] = [1, 2, 3, 4]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.containsDuplicate(nums)

    # assert
    assert expected == actual


def test_containsDuplicate_case_3():
    # arrange
    nums: list[int] = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.containsDuplicate(nums)

    # assert
    assert expected == actual
