class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        """time complexity: O(1), space complexity: O(1)"""
        # Step 1: Detect the cycle
        slow: int = nums[0]
        fast: int = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: Find the entry point
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate2(self, nums: list[int]) -> int:
        """time complexity: O(n), space complexity: O(n)"""
        d: dict[int, int] = {}
        for n in nums:
            if n in d:
                return n
            d[n] = 1
        return 0


def test_findDuplicate_case_1():
    # arrange
    nums: list[int] = [1, 3, 4, 2, 2]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.findDuplicate(nums)

    # assert
    assert expected == actual


def test_findDuplicate_case_2():
    # arrange
    nums: list[int] = [3, 1, 3, 4, 2]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.findDuplicate(nums)

    # assert
    assert expected == actual
