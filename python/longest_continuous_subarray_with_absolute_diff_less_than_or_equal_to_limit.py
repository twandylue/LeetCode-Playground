from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        # Time complexity: O(n)
        min_d: deque[int] = deque()
        max_d: deque[int] = deque()
        l: int = 0
        result: int = 0
        for r, num in enumerate(nums):
            while len(min_d) > 0 and min_d[-1] > num:
                min_d.pop()
            min_d.append(num)
            while len(max_d) > 0 and max_d[-1] < num:
                max_d.pop()
            max_d.append(num)
            while max_d[0] - min_d[0] > limit:
                if nums[l] == max_d[0]:
                    max_d.popleft()
                if nums[l] == min_d[0]:
                    min_d.popleft()
                l += 1
            result = max(r - l + 1, result)
        return result


def test_longestSubarray_case_1():
    # arrange
    nums: list[int] = [8, 2, 4, 7]
    limit: int = 4
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.longestSubarray(nums, limit)

    # assert
    assert expected == actual


def test_longestSubarray_case_2():
    # arrange
    nums: list[int] = [10, 1, 2, 4, 7, 2]
    limit: int = 5
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.longestSubarray(nums, limit)

    # assert
    assert expected == actual


def test_longestSubarray_case_3():
    # arrange
    nums: list[int] = [4, 2, 2, 2, 4, 4, 2, 2]
    limit: int = 0
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.longestSubarray(nums, limit)

    # assert
    assert expected == actual
