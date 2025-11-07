class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # Time complexity: O(n), Space complexity: O(n)
        prefix_sum: int = 0
        prefix_map: dict[int, int] = {0: 1}
        result: int = 0
        for num in nums:
            prefix_sum += 1 if num % 2 != 0 else 0
            result += prefix_map.get(prefix_sum - k, 0)
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return result


def test_numberOfSubarrays_1():
    # arrange
    nums: list[int] = [1, 1, 2, 1, 1]
    k: int = 3
    expected: int = 2

    # act
    actual = Solution().numberOfSubarrays(nums, k)

    # assert
    assert expected == actual


def test_numberOfSubarrays_2():
    # arrange
    nums: list[int] = [2, 4, 6]
    k: int = 1
    expected: int = 0

    # act
    actual = Solution().numberOfSubarrays(nums, k)

    # assert
    assert expected == actual


def test_numberOfSubarrays_3():
    # arrange
    nums: list[int] = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k: int = 2
    expected: int = 16

    # act
    actual = Solution().numberOfSubarrays(nums, k)

    # assert
    assert expected == actual
