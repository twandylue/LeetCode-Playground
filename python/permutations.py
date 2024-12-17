class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """time complexity: O(n! * n)"""
        result: list[list[int]] = []
        subset: list[int] = []
        pick: list[bool] = [False] * len(nums)
        self.dfs(subset, result, pick, nums)
        return result

    def dfs(
        self,
        subset: list[int],
        result: list[list[int]],
        pick: list[bool],
        nums: list[int],
    ) -> None:
        if len(subset) == len(nums):
            result.append(subset.copy())
            return
        for i in range(len(nums)):
            if pick[i]:
                continue
            subset.append(nums[i])
            pick[i] = True
            self.dfs(subset, result, pick, nums)
            subset.pop()
            pick[i] = False


def test_permute_case_1():
    # arrange
    nums: list[int] = [1, 2, 3]
    expected: list[list[int]] = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]

    # act
    solution = Solution()
    actual = solution.permute(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_permute_case_2():
    # arrange
    nums: list[int] = [0, 1]
    expected: list[list[int]] = [[0, 1], [1, 0]]

    # act
    solution = Solution()
    actual = solution.permute(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_permute_case_3():
    # arrange
    nums: list[int] = [1]
    expected: list[list[int]] = [[1]]

    # act
    solution = Solution()
    actual = solution.permute(nums)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
