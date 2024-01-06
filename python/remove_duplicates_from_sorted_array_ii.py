class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        r: int = 0
        l: int = 0
        while r < len(nums):
            count: int = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            for _ in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1

        return l


def test_removeDuplicates_case_1():
    # arrange
    nums: list[int] = [1, 1, 1, 2, 2, 3]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.removeDuplicates(nums)

    # assert
    assert expected == actual


def test_removeDuplicates_case_2():
    # arrange
    nums: list[int] = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    expected: int = 7

    # act
    solution = Solution()
    actual = solution.removeDuplicates(nums)

    # assert
    assert expected == actual
