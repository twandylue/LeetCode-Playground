class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        prefix_sum: int = 0
        prefix_map: dict[int, int] = {0: -1}
        result: int = 0
        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1
            if prefix_sum in prefix_map:
                result = max(result, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i
        return result


def test_findMaxLength_case_1():
    # arrange
    nums: list[int] = [0, 1]
    expected: int = 2

    # act
    actual: int = Solution().findMaxLength(nums)

    # assert
    assert expected == actual


def test_findMaxLength_case_2():
    # arrange
    nums: list[int] = [0, 1, 0]
    expected: int = 2

    # act
    actual: int = Solution().findMaxLength(nums)

    # assert
    assert expected == actual


def test_findMaxLength_case_3():
    # arrange
    nums: list[int] = [0, 1, 1, 1, 1, 1, 0, 0, 0]
    expected: int = 6

    # act
    actual: int = Solution().findMaxLength(nums)

    # assert
    assert expected == actual
