class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """time complexity: O(log n)"""
        l: int = 0
        r: int = len(nums) - 1
        while l <= r:
            mid: int = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


def test_search_case_1():
    # arrange
    nums: list[int] = [4, 5, 6, 7, 0, 1, 2]
    target: int = 0
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.search(nums, target)

    # assert
    assert expected == actual


def test_search_case_2():
    # arrange
    nums: list[int] = [4, 5, 6, 7, 0, 1, 2]
    target: int = 3
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.search(nums, target)

    # assert
    assert expected == actual


def test_search_case_3():
    # arrange
    nums: list[int] = [1]
    target: int = 0
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.search(nums, target)

    # assert
    assert expected == actual


def test_search_case_4():
    # arrange
    nums: list[int] = [5, 1, 3]
    target: int = 5
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.search(nums, target)

    # assert
    assert expected == actual
