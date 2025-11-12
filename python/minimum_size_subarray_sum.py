class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Time complexity: O(n)
        result: int = len(nums) + 1
        l: int = 0
        accu: int = 0
        for r in range(len(nums)):
            accu += nums[r]
            while accu >= target and l <= r:
                result = min(result, r - l + 1)
                accu -= nums[l]
                l += 1

        return 0 if result == len(nums) + 1 else result

    def minSubArrayLen2(self, target: int, nums: list[int]) -> int:
        # Time complexity: O(n log n), Space complexity: O(1)
        if sum(nums) < target:
            return 0
        l: int = 0
        r: int = len(nums)
        while l < r:
            mid: int = l + (r - l) // 2
            if self.feasible(mid, target, nums):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, size: int, target: int, nums: list[int]) -> bool:
        accu: int = 0
        for i in range(len(nums) - size + 1):
            accu = sum(nums[i : i + size])
            if accu >= target:
                return True
        return False


def test_minSubArrayLen_case_1():
    # arrange
    target: int = 7
    nums: list[int] = [2, 3, 1, 2, 4, 3]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual


def test_minSubArrayLen_case_2():
    # arrange
    target: int = 4
    nums: list[int] = [1, 4, 4]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual


def test_minSubArrayLen_case_3():
    # arrange
    target: int = 11
    nums: list[int] = [1, 1, 1, 1, 1, 1, 1, 1]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual


def test_minSubArrayLen_case_4():
    # arrange
    target: int = 11
    nums: list[int] = [1, 2, 3, 4, 5]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual


def test_minSubArrayLen_case_5():
    # arrange
    target: int = 15
    nums: list[int] = [1, 2, 3, 4, 5]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.minSubArrayLen(target, nums)

    # assert
    assert expected == actual
