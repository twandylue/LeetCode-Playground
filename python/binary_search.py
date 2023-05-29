class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1

        return -1


def test_binary_search_case1():
    # arrange
    nums: list[int] = [-1, 0, 3, 5, 9, 12]
    target: int = 9
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.search(nums, target)

    # assert
    assert actual == expected


def test_binary_search_case2():
    # arrange
    nums: list[int] = [-1, 0, 3, 5, 9, 12]
    target: int = 2
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.search(nums, target)

    # assert
    assert actual == expected
