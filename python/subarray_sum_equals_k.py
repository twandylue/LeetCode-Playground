class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result: int = 0
        prefix_map: dict[int, int] = {0: 1}  # prefix sum -> freq
        accu: int = 0
        for num in nums:
            accu += num
            remain: int = accu - k
            if remain in prefix_map:
                result += prefix_map[remain]
            if accu not in prefix_map:
                prefix_map[accu] = 1
            else:
                prefix_map[accu] += 1

        return result


def test_subarraySum_case_1():
    # arrange
    nums: list[int] = [1, 1, 1]
    k: int = 2
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.subarraySum(nums, k)

    # assert
    assert expected == actual


def test_subarraySum_case_2():
    # arrange
    nums: list[int] = [1, 2, 3]
    k: int = 3
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.subarraySum(nums, k)

    # assert
    assert expected == actual
