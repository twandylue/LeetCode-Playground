class Solution:
    def rearrangeArray2(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums) - 1):
            if 2 * nums[i] == nums[i - 1] + nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        for i in reversed(range(1, len(nums) - 1)):
            if 2 * nums[i] == nums[i - 1] + nums[i + 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

        return nums

    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result: list[int] = [0] * len(nums)
        nums.sort()
        h: int = 0
        if len(nums) % 2 > 0:
            h = (len(nums) - 1) // 2
        else:
            h = len(nums) // 2
        l: int = 0
        r: int = h
        for i in range(len(result)):
            if i % 2 == 0 and r < len(nums):
                result[i] = nums[r]
                r += 1
            elif i % 2 > 0 and l < h:
                result[i] = nums[l]
                l += 1

        return result


def test_rearrangeArray_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 4, 5]
    expected: list[int] = [3, 1, 4, 2, 5]

    # act
    solution = Solution()
    actual = solution.rearrangeArray(nums)

    # assert
    assert expected == actual


def test_rearrangeArray_case_2():
    # arrange
    nums: list[int] = [6, 2, 0, 9, 7]
    expected: list[int] = [6, 0, 7, 2, 9]

    # act
    solution = Solution()
    actual = solution.rearrangeArray(nums)

    # assert
    assert expected == actual


def test_rearrangeArray_case_3():
    # arrange
    nums: list[int] = [10, 7, 5, 4, 3]
    expected: list[int] = [5, 3, 7, 4, 10]

    # act
    solution = Solution()
    actual = solution.rearrangeArray(nums)

    # assert
    assert expected == actual
