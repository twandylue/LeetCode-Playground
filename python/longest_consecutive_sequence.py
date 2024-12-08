class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """time complexity: O(n), space complexity: O(n)"""
        result: int = 0
        nums_set: set[int] = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue
            length: int = 0
            while nums[i] + length in nums_set:
                length += 1
            result = max(result, length)

        return result


def test_longestConsecutive_case_1():
    # arrange
    nums: list[int] = [100, 4, 200, 1, 3, 2]
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.longestConsecutive(nums)

    # assert
    assert expected == actual


def test_longestConsecutive_case_2():
    # arrange
    nums: list[int] = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    expected: int = 9

    # act
    solution = Solution()
    actual = solution.longestConsecutive(nums)

    # assert
    assert expected == actual
