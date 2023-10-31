class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result: int = 0
        preAccuMap: dict[int, int] = {0: 1}
        accu: int = 0
        for i in range(len(nums)):
            accu += nums[i]
            remain: int = accu - k
            if remain in preAccuMap:
                result += preAccuMap[remain]

            if accu not in preAccuMap:
                preAccuMap[accu] = 1
            else:
                preAccuMap[accu] += 1

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
