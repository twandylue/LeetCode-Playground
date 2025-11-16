class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Time complexity: O(n), Space complexity: O(1)
        l: int = 0
        result: int = 0
        zero_count: int = 0
        for r in range(len(nums)):
            zero_count += 1 if nums[r] == 0 else 0
            while zero_count > k and l <= r:
                zero_count -= 1 if nums[l] == 0 else 0
                l += 1
            result = max(result, r - l + 1)
        return result


def test_longestOnes_case_1():
    # arrange
    nums: list[int] = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k: int = 2
    expected: int = 6

    # act
    actual = Solution().longestOnes(nums, k)

    # assert
    assert expected == actual


def test_longestOnes_case_2():
    # arrange
    nums: list[int] = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k: int = 3
    expected: int = 10

    # act
    actual = Solution().longestOnes(nums, k)

    # assert
    assert expected == actual
