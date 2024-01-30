class Solution:
    # NOTE: time complexity: O(n)
    def search(self, nums: list[int], target: int) -> bool:
        l: int = 0
        r: int = len(nums) - 1
        while l <= r:
            mid: int = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if target > nums[mid] and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1

        return False


def test_search_case_1():
    # arrange
    nums: list[int] = [2, 5, 6, 0, 0, 1, 2]
    target: int = 0
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.search(nums, target)

    # assert
    assert expected == actual


def test_search_case_2():
    # arrange
    nums: list[int] = [2, 5, 6, 0, 0, 1, 2]
    target: int = 3
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.search(nums, target)

    # assert
    assert expected == actual
