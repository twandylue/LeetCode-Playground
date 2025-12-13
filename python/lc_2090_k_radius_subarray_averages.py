class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        size: int = k * 2 + 1
        result: list[int] = [-1] * len(nums)
        accu: int = 0
        l: int = 0
        for r in range(len(nums)):
            accu += nums[r]
            if r - l + 1 == size:
                index: int = l + (r - l) // 2
                avg: int = accu // size
                result[index] = avg
                accu -= nums[l]
                l += 1
        return result


def test_getAverages_case_1():
    # arrange
    nums: list[int] = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k: int = 3
    expected: list[int] = [-1, -1, -1, 5, 4, 4, -1, -1, -1]

    # act
    solution = Solution()
    actual = solution.getAverages(nums, k)

    # assert
    assert expected == actual


def test_getAverages_case_2():
    # arrange
    nums: list[int] = [100000]
    k: int = 0
    expected: list[int] = [100000]

    # act
    solution = Solution()
    actual = solution.getAverages(nums, k)

    # assert
    assert expected == actual


def test_getAverages_case_3():
    # arrange
    nums: list[int] = [8]
    k: int = 100000
    expected: list[int] = [-1]

    # act
    solution = Solution()
    actual = solution.getAverages(nums, k)

    # assert
    assert expected == actual
