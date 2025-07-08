class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result: list[int] = [nums[0]]
        for i in range(1, len(nums)):
            result.append(result[i - 1] + nums[i])
        return result


def test_runningSum_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 4]
    expected: list[int] = [1, 3, 6, 10]

    # act
    actual = Solution().runningSum(nums)

    # assert
    assert expected == actual


def test_runningSum_case_2():
    # arrange
    nums: list[int] = [1, 1, 1, 1, 1]
    expected: list[int] = [1, 2, 3, 4, 5]

    # act
    actual = Solution().runningSum(nums)

    # assert
    assert expected == actual


def test_runningSum_case_3():
    # arrange
    nums: list[int] = [3, 1, 2, 10, 1]
    expected: list[int] = [3, 4, 6, 16, 17]

    # act
    actual = Solution().runningSum(nums)

    # assert
    assert expected == actual
