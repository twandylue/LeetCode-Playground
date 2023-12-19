class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total: int = sum(nums)
        curr_sum: int = 0
        for i in range(len(nums)):
            if float(total - nums[i]) / 2 == float(curr_sum):
                return i
            curr_sum += nums[i]

        return -1


def test_pivotIndex_case_1():
    # arrange
    nums: list[int] = [1, 7, 3, 6, 5, 6]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.pivotIndex(nums)

    # assert
    assert expected == actual


def test_pivotIndex_case_2():
    # arrange
    nums: list[int] = [1, 2, 3]
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.pivotIndex(nums)

    # assert
    assert expected == actual


def test_pivotIndex_case_3():
    # arrange
    nums: list[int] = [2, 1, -1]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.pivotIndex(nums)

    # assert
    assert expected == actual
