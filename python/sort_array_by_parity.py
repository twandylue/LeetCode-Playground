class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """time complexity: O(n)"""
        r: int = 0
        l: int = 0
        while r < len(nums) and l < len(nums):
            if nums[r] % 2 == 0:
                tmp: int = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                l += 1
            r += 1
        return nums


def test_sortArrayByParity_case_1():
    # arrange
    nums: list[int] = [3, 1, 2, 4]
    expected: list[int] = [2, 4, 3, 1]

    # act
    solution = Solution()
    actual: list[int] = solution.sortArrayByParity(nums)

    # assert
    assert expected == nums


def test_sortArrayByParity_case_2():
    # arrange
    nums: list[int] = [0, 1, 2]
    expected: list[int] = [0, 2, 1]

    # act
    solution = Solution()
    actual: list[int] = solution.sortArrayByParity(nums)

    # assert
    assert expected == nums
