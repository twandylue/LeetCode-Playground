class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis: list[int] = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)


def test_lengthOfLIS_case_1():
    # arrange
    nums: list[int] = [10, 9, 2, 5, 3, 7, 101, 18]
    expected: int = 4

    # act
    solution = Solution()
    actual: int = solution.lengthOfLIS(nums)

    # assert
    assert actual == expected


def test_lengthOfLIS_case_2():
    # arrange
    nums: list[int] = [0, 1, 0, 3, 2, 3]
    expected: int = 4

    # act
    solution = Solution()
    actual: int = solution.lengthOfLIS(nums)

    # assert
    assert actual == expected


def test_lengthOfLIS_case_3():
    # arrange
    nums: list[int] = [7, 7, 7, 7, 7, 7, 7]
    expected: int = 1

    # act
    solution = Solution()
    actual: int = solution.lengthOfLIS(nums)

    # assert
    assert actual == expected
