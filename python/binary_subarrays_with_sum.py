class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """time complexity: O(n)"""
        return self.helper(nums, goal) - self.helper(nums, goal - 1)

    def helper(self, nums: list[int], x: int) -> int:
        """Count numbers of subarrays where curr <= x"""
        if x < 0:
            return 0
        l: int = 0
        curr: int = 0
        result: int = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > x:
                curr -= nums[l]
                l += 1
            result += r - l + 1
        return result


def test_numSubarraysWithSum_case_1():
    """This is a test case"""
    # arrange
    nums: list[int] = [1, 0, 1, 0, 1]
    goal: int = 2
    expected: int = 4

    # act
    actual = Solution().numSubarraysWithSum(nums, goal)

    # assert
    assert expected == actual


def test_numSubarraysWithSum_case_2():
    """This is a test case"""
    # arrange
    nums: list[int] = [0, 0, 0, 0, 0]
    goal: int = 0
    expected: int = 15

    # act
    actual = Solution().numSubarraysWithSum(nums, goal)

    # assert
    assert expected == actual
