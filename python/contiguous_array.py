class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # Time complexity: O(n)
        prefix_map: dict[int, int] = {0: -1}
        accu: int = 0
        result: int = 0
        for i, num in enumerate(nums):
            accu += 1 if num == 1 else -1
            if accu in prefix_map:
                result = max(result, i - prefix_map[accu])
            else:
                prefix_map[accu] = i
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
