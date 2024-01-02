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
        result: list[int] = list()
        nums.sort()
        l: int = 0
        r: int = len(nums) - 1
        while len(result) != len(nums):
            result.append(nums[l])
            l += 1

            if l < r:
                result.append(nums[r])
                r -= 1

        return result


def test_rearrangeArray_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 4, 5]
    expected: list[int] = [1, 5, 2, 4, 3]

    # act
    solution = Solution()
    actual = solution.rearrangeArray(nums)

    # assert
    assert expected == actual


def test_rearrangeArray_case_2():
    # arrange
    nums: list[int] = [6, 2, 0, 9, 7]
    expected: list[int] = [0, 9, 2, 7, 6]

    # act
    solution = Solution()
    actual = solution.rearrangeArray(nums)

    # assert
    assert expected == actual


def test_rearrangeArray_case_3():
    # arrange
    nums: list[int] = [10, 7, 5, 4, 3]
    expected: list[int] = [10, 5, 7, 3, 4]

    # act
    solution = Solution()
    actual = solution.rearrangeArray2(nums)

    # assert
    assert expected == actual
