class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        l: int = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                continue

            nums[l] = nums[r]
            l += 1

        for i in range(l, len(nums)):
            nums[i] = 0

        return nums


def test_applyOperations_case_1():
    # arrange
    nums: list[int] = [1, 2, 2, 1, 1, 0]
    expected: list[int] = [1, 4, 2, 0, 0, 0]

    # act
    solution = Solution()
    actual = solution.applyOperations(nums)

    # assert
    assert expected == actual
