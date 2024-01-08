class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result: int = len(nums) + 1
        l: int = 0
        accu: int = 0
        for r in range(len(nums)):
            accu += nums[r]
            while accu >= target:
                result = min(result, r - l + 1)
                accu -= nums[l]
                l += 1

        return 0 if result == len(nums) + 1 else result


def test_minSubArrayLen_case_1():
    # arrange
    target: int = 7
    nums: list[int] = [2, 3, 1, 2, 4, 3]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual


def test_minSubArrayLen_case_2():
    # arrange
    target: int = 4
    nums: list[int] = [1, 4, 4]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual


def test_minSubArrayLen_case_3():
    # arrange
    target: int = 11
    nums: list[int] = [1, 1, 1, 1, 1, 1, 1, 1]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual


def test_minSubArrayLen_case_4():
    # arrange
    target: int = 11
    nums: list[int] = [1, 2, 3, 4, 5]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual


def test_minSubArrayLen_case_5():
    # arrange
    target: int = 15
    nums: list[int] = [1, 2, 3, 4, 5]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual
