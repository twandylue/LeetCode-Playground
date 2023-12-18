class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        numMap: dict[int, int] = dict()
        for i in range(len(nums)):
            if nums[i] not in numMap:
                numMap[nums[i]] = 1
            else:
                numMap[nums[i]] += 1
                if numMap[nums[i]] > len(nums) / 2:
                    return nums[i]
        return 0


def test_majorityElement_case_1():
    # arrange
    nums: list[int] = [3, 2, 3]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.majorityElement(nums)

    # assert
    assert expected == actual


def test_majorityElement_case_2():
    # arrange
    nums: list[int] = [2, 2, 1, 1, 1, 2, 2]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.majorityElement(nums)

    # assert
    assert expected == actual
