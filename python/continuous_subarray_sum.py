class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """time complexity: O(n)"""
        remain_map: dict[int, int] = {0: -1}
        total: int = 0
        for i, n in enumerate(nums):
            total += n
            remain: int = total % k
            if remain not in remain_map:
                remain_map[remain] = i
            elif i - remain_map[remain] > 1:
                return True
        return False

    def checkSubarraySum2(self, nums: list[int], k: int) -> bool:
        prefix_sum: int = 0
        prefix_map: dict[int, int] = {0: -1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum % k in prefix_map and i - prefix_map[prefix_sum % k] >= 2:
                return True
            if prefix_sum % k not in prefix_map:
                prefix_map[prefix_sum % k] = i
        return False


def test_checkSubarraySum_case_1():
    # arrange
    nums: list = [23, 2, 4, 6, 7]
    k: int = 6
    expected: bool = True

    # act
    actual = Solution().checkSubarraySum(nums, k)

    # assert
    assert actual == expected


def test_checkSubarraySum_case_2():
    # arrange
    nums: list = [23, 2, 6, 4, 7]
    k: int = 13
    expected: bool = False

    # act
    actual = Solution().checkSubarraySum(nums, k)

    # assert
    assert actual == expected


def test_checkSubarraySum_case_3():
    # arrange
    nums: list = [23, 2, 6, 4, 7]
    k: int = 13
    expected: bool = False

    # act
    actual = Solution().checkSubarraySum2(nums, k)

    # assert
    assert actual == expected
