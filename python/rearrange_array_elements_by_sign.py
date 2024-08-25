class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """time complexity: O(n)"""
        i: int = 0
        j: int = 1
        result: list[int] = [0] * len(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                result[i] = nums[k]
                i += 2
            else:
                result[j] = nums[k]
                j += 2
        return result


def test_rearrangeArray_case_1():
    # arrange
    nums: list[int] = [3, 1, -2, -5, 2, -4]
    expected: list[int] = [3, -2, 1, -5, 2, -4]

    # act
    actual: list[int] = Solution().rearrangeArray(nums)

    # assert
    assert expected == actual


def test_rearrangeArray_case_2():
    # arrange
    nums: list[int] = [-1, 1]
    expected: list[int] = [1, -1]

    # act
    actual: list[int] = Solution().rearrangeArray(nums)

    # assert
    assert expected == actual
