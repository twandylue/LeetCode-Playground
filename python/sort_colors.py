class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0,2,1,2]
        l: int = 0
        m: int = 0
        r: int = len(nums) - 1
        while m <= r:
            if nums[m] == 0:
                tmp: int = nums[m]
                nums[m] = nums[l]
                nums[l] = tmp
                l += 1
                # m += 1
                m = l
            elif nums[m] == 2:
                tmp: int = nums[m]
                nums[m] = nums[r]
                nums[r] = tmp
                r -= 1
            else:
                m += 1


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
