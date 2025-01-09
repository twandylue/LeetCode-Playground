class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """time complexity: O(n)"""
        result: list[int] = [0] * len(nums)
        left: int = 1
        for i in range(0, len(nums)):
            result[i] = left
            left *= nums[i]
        right: int = 1
        right_to_left: list[int] = [0] * len(nums)
        for i in reversed(range(0, len(nums))):
            right_to_left[i] = right
            right *= nums[i]
        for i in range(len(result)):
            result[i] *= right_to_left[i]
        return result


def test_productExceptSelf_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 4]
    expected: list[int] = [24, 12, 8, 6]

    # act
    solution = Solution()
    actual = solution.productExceptSelf(nums)

    # assert
    assert expected == actual


def test_productExceptSelf_case_2():
    # arrange
    nums: list[int] = [-1, 1, 0, -3, 3]
    expected: list[int] = [0, 0, 9, 0, 0]

    # act
    solution = Solution()
    actual = solution.productExceptSelf(nums)

    # assert
    assert expected == actual
