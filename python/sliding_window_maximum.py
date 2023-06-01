# TODO: test
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        results: list[int] = []
        q: dict[int] = collections.deque()
        l = 0
        for r in range(len(nums)):
            while len(q) > 0 and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                results.append(nums[q[0]])
                l += 1

        return results


def test_two_sum_2_case1():
    # arrange
    numbers: list[int] = [1,3,-1,-3,5,3,6,7]
    k: int = 3
    expected: list[int] = [3,3,5,5,6,7]

    # act
    solution = Solution()
    actual = solution.maxSlidingWindow(numbers, k)

    # assert
    assert actual == expected


def test_two_sum_2_case2():
    # arrange
    numbers: list[int] = [1]
    target: int = 1
    expected: list[int] = [1]

    # act
    solution = Solution()
    actual = solution.maxSlidingWindow(numbers, k)

    # assert
    assert actual == expected
