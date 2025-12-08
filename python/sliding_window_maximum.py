from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """time complexity: O(n)"""
        result: list[int] = []
        queue: deque[int] = deque()
        for i, num in enumerate(nums):
            while len(queue) > 0 and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if queue[0] <= i - k:
                queue.popleft()
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result

    def maxSlidingWindow2(self, nums: list[int], k: int) -> list[int]:
        """time complexity: O(n)"""
        result: list[int] = []
        max_deque: deque[int] = deque()
        l: int = 0
        for r in range(len(nums)):
            while len(max_deque) > 0 and nums[max_deque[-1]] < nums[r]:
                max_deque.pop()
            max_deque.append(r)
            if l - 1 == max_deque[0]:
                max_deque.popleft()
            print(f"r: {r}, l: {l}")
            if r - l + 1 == k:
                result.append(nums[max_deque[0]])
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


def test_maxSlidingWindow_case3():
    # arrange
    numbers: list[int] = [1]
    k: int = 1
    expected: list[int] = [1]

    # act
    solution = Solution()
    actual = solution.maxSlidingWindow(numbers, k)

    # assert
    assert actual == expected


def test_maxSlidingWindow_case_4():
    # arrange
    numbers: list[int] = [1, 3, -1, -3, 5, 3, 6, 7]
    k: int = 3
    expected: list[int] = [3, 3, 5, 5, 6, 7]

    # act
    solution = Solution()
    actual = solution.maxSlidingWindow2(numbers, k)

    # assert
    assert actual == expected
