class Solution:
    # NOTE: also works but not concise.
    # def searchInsert(self, nums: list[int], target: int) -> int:
    #     mid: int = 0
    #     l: int = 0
    #     r: int = len(nums) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] < target:
    #             if mid < len(nums) - 1 and target < nums[mid + 1]:
    #                 return mid + 1
    #             l = mid + 1
    #         else:
    #             if mid > 0 and target > nums[mid - 1]:
    #                 return mid
    #             r = mid - 1
    #
    #     return 0 if mid == 0 and nums[mid] > target else mid + 1

    def searchInsert(self, nums: list[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1
        result: int = -1
        while l <= r:
            mid: int = (l + r) // 2
            result = mid
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return result + 1 if nums[result] < target else result


def test_searchInsert_case_1():
    # arrange
    nums: list[int] = [1, 3, 5, 6]
    target: int = 5
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.searchInsert(nums, target)

    # assert
    assert expected == actual


def test_searchInsert_case_2():
    # arrange
    nums: list[int] = [1, 3, 5, 6]
    target: int = 2
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.searchInsert(nums, target)

    # assert
    assert expected == actual


def test_searchInsert_case_3():
    # arrange
    nums: list[int] = [1, 3, 5, 6]
    target: int = 7
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.searchInsert(nums, target)

    # assert
    assert expected == actual


def test_searchInsert_case_4():
    # arrange
    nums: list[int] = [1]
    target: int = 2
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.searchInsert(nums, target)

    # assert
    assert expected == actual


def test_searchInsert_case_5():
    # arrange
    nums: list[int] = [1, 3]
    target: int = 2
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.searchInsert(nums, target)

    # assert
    assert expected == actual


def test_searchInsert_case_6():
    # arrange
    nums: list[int] = [2, 3, 5]
    target: int = 1
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.searchInsert(nums, target)

    # assert
    assert expected == actual


def test_searchInsert_case_7():
    # arrange
    nums: list[int] = [3, 5, 7, 9, 10]
    target: int = 8
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.searchInsert(nums, target)

    # assert
    assert expected == actual
