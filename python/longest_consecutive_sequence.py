class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """time complexity: O(n), space complexity: O(n)"""
        result: int = 0
        nums_set: set[int] = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            count: int = 1
            while num + 1 in nums_set:
                num = num + 1
                count += 1
            result = max(result, count)

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
