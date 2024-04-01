class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l: int = 0
        r: int = len(nums) - 1
        mid: int = 0
        while l <= r:
            mid = (l + r) // 2
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                return mid
        return mid


def test_findPeakElement_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 1]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.findPeakElement(nums)

    # assert
    assert expected == actual


def test_findPeakElement_case_2():
    # arrange
    nums: list[int] = [1, 2, 1, 3, 5, 6, 4]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.findPeakElement(nums)

    # assert
    assert expected == actual


def test_findPeakElement_case_3():
    # arrange
    nums: list[int] = [1]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.findPeakElement(nums)

    # assert
    assert expected == actual


def test_findPeakElement_case_4():
    # arrange
    nums: list[int] = [1, 2]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.findPeakElement(nums)

    # assert
    assert expected == actual
