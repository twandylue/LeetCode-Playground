class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet: set[int] = set(nums)
        result: int = 0
        for num in nums:
            if num - 1 not in numSet:
                length: int = 0
                while num + length in numSet:
                    length += 1

                result = max(result, length)

            ## NOTE: over time
            # if num in numSet:
            #     length: int = 0
            #     while num in numSet:
            #         num += 1
            #         length += 1
            #     result = max(result, length)

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
