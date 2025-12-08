from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        # Time complexity: O(n)
        min_queue: deque[int] = deque()
        max_queue: deque[int] = deque()
        result: int = 0
        l: int = 0
        for r, num in enumerate(nums):
            while len(min_queue) > 0 and min_queue[-1] > num:
                min_queue.pop()
            min_queue.append(num)
            while len(max_queue) > 0 and max_queue[-1] < num:
                max_queue.pop()
            max_queue.append(num)
            while max_queue[0] - min_queue[0] > limit:
                if nums[l] == max_queue[0]:
                    max_queue.popleft()
                if nums[l] == min_queue[0]:
                    min_queue.popleft()
                l += 1
            result = max(result, r - l + 1)

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
