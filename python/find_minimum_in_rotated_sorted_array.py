class Solution:
    def findMin(self, nums: list[int]) -> int:
        """time complexity: O(log n)"""
        l: int = 0
        r: int = len(nums) - 1
        result: int = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid: int = int((l + r) / 2)
            result = min(result, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return result


def test_findMin_case_1():
    # arrange
    nums: list[int] = [3, 4, 5, 1, 2]
    expected: int = 1

    # act
    actual = Solution().findMin(nums)

    # assert
    assert expected == actual


def test_findMin_case_2():
    # arrange
    nums: list[int] = [4, 5, 6, 7, 0, 1, 2]
    expected: int = 0

    # act
    actual = Solution().findMin(nums)

    # assert
    assert expected == actual


def test_findMin_case_3():
    # arrange
    nums: list[int] = [11, 13, 15, 17]
    expected: int = 11

    # act
    actual = Solution().findMin(nums)

    # assert
    assert expected == actual
