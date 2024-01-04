class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l: int = 0
        i: int = 0
        r: int = len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1


def test_sortColors_case_1():
    # arrange
    nums: list[int] = [2, 0, 2, 1, 1, 0]
    expected: list[list[int]] = [0, 0, 1, 1, 2, 2]

    # act
    solution = Solution()
    solution.sortColors(nums)

    # assert
    assert expected == nums


def test_sortColors_case_2():
    # arrange
    nums: list[int] = [2, 0, 1]
    expected: list[list[int]] = [0, 1, 2]

    # act
    solution = Solution()
    solution.sortColors(nums)

    # assert
    assert expected == nums


def test_sortColors_case_3():
    # arrange
    nums: list[int] = [1, 0, 2]
    expected: list[list[int]] = [0, 1, 2]

    # act
    solution = Solution()
    solution.sortColors(nums)

    # assert
    assert expected == nums


def test_sortColors_case_4():
    # arrange
    nums: list[int] = [1, 2, 0]

    expected: list[list[int]] = [0, 1, 2]

    # act
    solution = Solution()
    solution.sortColors(nums)

    # assert
    assert expected == nums
