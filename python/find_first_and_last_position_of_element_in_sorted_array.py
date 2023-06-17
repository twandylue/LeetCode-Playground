class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)

        return [left, right]

    def binSearch(self, nums: list[int], target: int, leftBias: bool) -> int:
        output = -1
        if len(nums) == 0:
            return output

        l = 0
        r = len(nums) - 1
        while l <= r and r < len(nums):
            mid = (l + r) // 2
            if nums[mid] == target:
                output = mid
                if leftBias:
                    if mid > 0:
                        r = mid - 1
                        l = 0
                    else:
                        break
                else:
                    l = mid + 1
                    r = len(nums) - 1
            elif nums[mid] > target:
                if mid > 0:
                    r = mid - 1
                else:
                    break
            else:
                l = mid + 1

        return output


def test_searchRange_case_1():
    # arrange
    nums: list[int] = [5, 7, 7, 8, 8, 10]
    target: int = 8
    expected: list[int] = [3, 4]

    # act
    solution = Solution()
    actual = solution.searchRange(nums, target)

    # assert
    assert actual == expected


def test_searchRange_case_2():
    # arrange
    nums: list[int] = [5, 7, 7, 8, 8, 10]
    target: int = 6
    expected: list[int] = [-1, -1]

    # act
    solution = Solution()
    actual = solution.searchRange(nums, target)

    # assert
    assert actual == expected


def test_searchRange_case_3():
    # arrange
    nums: list[int] = []
    target: int = 0
    expected: list[int] = [-1, -1]

    # act
    solution = Solution()
    actual = solution.searchRange(nums, target)

    # assert
    assert actual == expected
