class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """time complexity: O(n)"""
        if len(nums) == 0:
            return []
        result: list[str] = []
        left: int = 0
        right: int = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                right = i
                continue
            if right > left:
                result.append(f"{nums[left]}->{nums[right]}")
            else:
                result.append(f"{nums[left]}")
            left = i
        if right > left:
            result.append(f"{nums[left]}->{nums[right]}")
        else:
            result.append(f"{nums[left]}")
        return result

    def summaryRanges2(self, nums: list[int]) -> list[str]:
        """time complexity: O(n)"""
        ranges: list[list[int]] = []
        for num in nums:
            if len(ranges) > 0 and ranges[-1][1] == num - 1:
                ranges[-1][1] = num
            else:
                ranges.append([num, num])
        return [f"{x}->{y}" if x != y else f"{x}" for x, y in ranges]


def test_summaryRanges_case_1():
    # arrange
    nums: list[int] = [0, 1, 2, 4, 5, 7]
    expected: list[str] = ["0->2", "4->5", "7"]

    # act
    actual = Solution().summaryRanges(nums)

    # assert
    assert actual == expected


def test_summaryRanges_case_2():
    # arrange
    nums: list[int] = [0, 1, 2, 4, 5, 7]
    expected: list[str] = ["0->2", "4->5", "7"]

    # act
    actual = Solution().summaryRanges2(nums)

    # assert
    assert actual == expected


def test_summaryRanges_case_3():
    # arrange
    nums: list[int] = [0, 2, 3, 4, 6, 8, 9]
    expected: list[str] = ["0", "2->4", "6", "8->9"]

    # act
    actual = Solution().summaryRanges(nums)

    # assert
    assert actual == expected


def test_summaryRanges_case_4():
    # arrange
    nums: list[int] = [0, 2, 3, 4, 6, 8, 9]
    expected: list[str] = ["0", "2->4", "6", "8->9"]

    # act
    actual = Solution().summaryRanges2(nums)

    # assert
    assert actual == expected
