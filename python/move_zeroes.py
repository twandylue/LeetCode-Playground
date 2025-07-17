class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_none_zero: int = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[last_none_zero] = nums[i]
            last_none_zero += 1
        for i in range(last_none_zero, len(nums)):
            nums[i] = 0

    def moveZeroes2(self, nums: list[int]) -> None:
        """
        Time Complexity: O(n)
        """
        l: int = 0
        r: int = 0
        while r < len(nums):
            if nums[r] == 0:
                r += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
        while r < len(nums):
            nums[r] = 0


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
