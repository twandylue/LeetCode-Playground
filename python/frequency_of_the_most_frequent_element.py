class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        result: int = 0
        nums.sort()
        l: int = 0
        accu: int = 0
        for r in range(len(nums)):
            currLen: int = r - l + 1
            accu += nums[r]
            while currLen * nums[r] > accu + k:
                accu -= nums[l]
                l += 1
                currLen -= 1

            result = max(result, currLen)

        return result


def test_maxFrequency_case1():
    # arrange
    nums: list[int] = [1, 2, 4]
    k: int = 5
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.maxFrequency(nums, k)

    # assert
    assert expected == actual


def test_maxFrequency_case2():
    # arrange
    nums: list[int] = [1, 4, 8, 13]
    k: int = 5
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.maxFrequency(nums, k)

    # assert
    assert expected == actual


def test_maxFrequency_case3():
    # arrange
    nums: list[int] = [3, 9, 6]
    k: int = 2
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.maxFrequency(nums, k)

    # assert
    assert expected == actual
