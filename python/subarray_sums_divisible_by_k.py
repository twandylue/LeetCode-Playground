class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # Time complexity: O(n), Sapce complexity: O(1)
        prefix_sum: int = 0
        prefix_map: dict[int, int] = {0: 1}
        result: int = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum % k in prefix_map:
                result += prefix_map[prefix_sum % k]
            prefix_map[prefix_sum % k] = prefix_map.get(prefix_sum % k, 0) + 1
        return result


def test_subarraysDivByK_1():
    # arrange
    nums: list[int] = [4, 5, 0, -2, -3, 1]
    k: int = 5
    expected: int = 7

    # act
    actual = Solution().subarraysDivByK(nums, k)

    # assert
    assert expected == actual


def test_subarraysDivByK_2():
    # arrange
    nums: list[int] = [5]
    k: int = 9
    expected: int = 0

    # act
    actual = Solution().subarraysDivByK(nums, k)

    # assert
    assert expected == actual
