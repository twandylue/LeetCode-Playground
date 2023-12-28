class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l: int = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                continue
            nums[l] = nums[r]
            l += 1

        while l < len(nums):
            nums[l] = 0
            l += 1


def test_moveZeroes_case_1():
    # arrange
    nums: list[int] = [0, 1, 0, 3, 12]
    expected: list[int] = [1, 3, 12, 0, 0]

    # act
    solution = Solution()
    solution.moveZeroes(nums)

    # assert
    assert expected == nums


def test_moveZeroes_case_2():
    # arrange
    nums: list[int] = [0]
    expected: list[int] = [0]

    # act
    solution = Solution()
    solution.moveZeroes(nums)

    # assert
    assert expected == nums


def test_moveZeroes_case_3():
    # arrange
    nums: list[int] = [1]
    expected: list[int] = [1]

    # act
    solution = Solution()
    solution.moveZeroes(nums)

    # assert
    assert expected == nums


def test_moveZeroes_case_4():
    # arrange
    nums: list[int] = [1, 0]
    expected: list[int] = [1, 0]

    # act
    solution = Solution()
    solution.moveZeroes(nums)

    # assert
    assert expected == nums


def test_moveZeroes_case_5():
    # arrange
    nums: list[int] = [1, 0, 1]
    expected: list[int] = [1, 1, 0]

    # act
    solution = Solution()
    solution.moveZeroes(nums)

    # assert
    assert expected == nums
