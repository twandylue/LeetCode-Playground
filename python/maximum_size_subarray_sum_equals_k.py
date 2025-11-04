class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        # Time complexity: O(n), Space complexity: O(n)
        prefix_accu: int = 0
        prefix_map: dict[int, int] = {0: -1}
        result: int = 0
        for i in range(len(nums)):
            prefix_accu += nums[i]
            if prefix_accu - k in prefix_map:
                result = max(result, i - prefix_map[prefix_accu - k])
            if prefix_accu not in prefix_map:
                prefix_map[prefix_accu] = i
        return result


def test_maxSubArrayLen_1():
    # arrange
    nums: list[int] = [1, -1, 5, -2, 3]
    target: int = 3
    expected: int = 4

    # act
    actual = Solution().maxSubArrayLen(nums, target)

    # assert
    assert expected == actual


def test_maxSubArrayLen_2():
    # arrange
    nums: list[int] = [2, 3, 4]
    target: int = 10
    expected: int = 0

    # act
    actual = Solution().maxSubArrayLen(nums, target)

    # assert
    assert expected == actual
