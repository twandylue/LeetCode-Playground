class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """time complexity: O(n)"""
        l: int = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l


def test_removeDuplicates_case_1():
    # arrange
    nums: list[int] = [1, 1, 2]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.removeDuplicates(nums)

    # assert
    assert expected == actual


def test_removeDuplicates_case_2():
    # arrange
    nums: list[int] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.removeDuplicates(nums)

    # assert
    assert expected == actual
