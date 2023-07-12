class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        subset: list[int] = []

        self.dfs(0, nums, subset, result)

        return result

    def dfs(
        self, i: int, nums: list[int], subset: list[int], result: list[list[int]]
    ) -> None:
        if i >= len(nums):
            result.append(subset[::])
            return

        subset.append(nums[i])
        self.dfs(i + 1, nums, subset, result)
        subset.pop()
        self.dfs(i + 1, nums, subset, result)


def test_subsets_case_1():
    # arrange
    nums: list[int] = [1, 2, 3]
    expected: list[list[int]] = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    # act
    solution = Solution()
    actual = solution.subsets(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_subsets_case_2():
    # arrange
    nums: list[int] = [0]
    expected: list[list[int]] = [[], [0]]

    # act
    solution = Solution()
    actual = solution.subsets(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
