class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        # Time complexity: O(n log n + n log d) where n is the length of nums and d is the range of distances,
        # d is the range of values (max(nums) - min(nums))
        # Space complexity: O(1)
        nums.sort()
        l: int = 0
        r: int = nums[-1] - nums[0]
        while l < r:
            mid: int = l + (r - l) // 2
            if self.feasible(mid, nums, k):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, val: int, nums: list[int], k: int) -> bool:
        count: int = 0
        i: int = 0
        j: int = 0
        while i < len(nums) or j < len(nums):
            while j < len(nums) and nums[j] - nums[i] <= val:
                j += 1
            count += j - i - 1
            i += 1
        return count >= k


def test_smallestDistancePair_1():
    # arrange
    nums: list[int] = [1, 3, 1]
    k: int = 1
    expected: int = 0

    # act
    actual = Solution().smallestDistancePair(nums, k)

    # assert
    assert expected == actual


def test_smallestDistancePair_2():
    # arrange
    nums: list[int] = [1, 1, 1]
    k: int = 2
    expected: int = 0

    # act
    actual = Solution().smallestDistancePair(nums, k)

    # assert
    assert expected == actual


def test_smallestDistancePair_3():
    # arrange
    nums: list[int] = [1, 6, 1]
    k: int = 3
    expected: int = 5

    # act
    actual = Solution().smallestDistancePair(nums, k)

    # assert
    assert expected == actual
