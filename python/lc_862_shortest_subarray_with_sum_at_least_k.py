from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        result = float("inf")
        min_deque: deque[int] = deque()
        n: int = len(nums)
        prefix_sum: list[int] = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        for r in range(n + 1):
            while len(min_deque) > 0 and prefix_sum[r] - prefix_sum[min_deque[0]] >= k:
                result = min(result, r - min_deque[0])
                min_deque.popleft()
            while len(min_deque) > 0 and prefix_sum[min_deque[-1]] > prefix_sum[r]:
                min_deque.pop()
            min_deque.append(r)
        return result if result != float("inf") else -1


def test_shortestSubarray_case_1():
    # arrange
    nums: list[int] = [1]
    k: int = 1
    expected: int = 1

    # act
    actual = Solution().shortestSubarray(nums, k)

    # assert
    assert expected == actual


def test_shortestSubarray_case_2():
    # arrange
    nums: list[int] = [1, 2]
    k: int = 4
    expected: int = -1

    # act
    actual = Solution().shortestSubarray(nums, k)

    # assert
    assert expected == actual


def test_shortestSubarray_case_3():
    # arrange
    nums: list[int] = [2, -1, 2]
    k: int = 3
    expected: int = 3

    # act
    actual = Solution().shortestSubarray(nums, k)

    # assert
    assert expected == actual
