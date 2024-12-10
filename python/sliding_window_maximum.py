from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """time complexity: O(n)"""
        result: int = list()
        queue: deque[int] = deque()
        l: int = 0
        for r in range(len(nums)):
            while len(queue) > 0 and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)
            if l > queue[0]:
                queue.popleft()
            if (r + 1) >= k:
                result.append(nums[queue[0]])
                l += 1

        return result


def test_maxSlidingWindow_case_1():
    # arrange
    numbers: list[int] = [1, 3, -1, -3, 5, 3, 6, 7]
    k: int = 3
    expected: list[int] = [3, 3, 5, 5, 6, 7]

    # act
    solution = Solution()
    actual = solution.maxSlidingWindow(numbers, k)

    # assert
    assert actual == expected


def test_maxSlidingWindow_case2():
    # arrange
    numbers: list[int] = [1]
    k: int = 1
    expected: list[int] = [1]

    # act
    solution = Solution()
    actual = solution.maxSlidingWindow(numbers, k)

    # assert
    assert actual == expected
