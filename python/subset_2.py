class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        nums.sort()  # sort the input to handle duplicates
        self.bfs(0, nums, [], result)
        return result

    def bfs(
        self, i: int, nums: list[int], subset: list[int], result: list[list[int]]
    ) -> None:
        if i == len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[i])
        self.bfs(i + 1, nums, subset, result)
        subset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.bfs(i + 1, nums, subset, result)


def test_subsetsWithDup_case_1():
    # arrange
    nums: list[int] = [1, 2, 2]
    expected: list[list[int]] = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    # act
    solution = Solution()
    actual = solution.subsetsWithDup(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_subsetsWithDup_case_2():
    # arrange
    nums: list[int] = [0]
    expected: list[list[int]] = [[], [0]]

    # act
    solution = Solution()
    actual = solution.subsetsWithDup(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
