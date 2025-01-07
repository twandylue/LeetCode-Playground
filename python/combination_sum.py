class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """time complexity: O(2^(t/m)) where t is the target and m is the min value in candidates"""
        result: list[list[int]] = []
        subset: list[int] = []
        accu: int = 0
        self.dfs(0, accu, subset, result, candidates, target)
        return result

    def dfs(
        self,
        i: int,
        accu: int,
        subset: list[int],
        result: list[list[int]],
        candidates: list[int],
        target: int,
    ) -> None:
        if accu == target:
            result.append(subset.copy())
            return
        if i >= len(candidates) or accu > target:
            return
        subset.append(candidates[i])
        self.dfs(i, accu + candidates[i], subset, result, candidates, target)
        subset.pop()
        self.dfs(i + 1, accu, subset, result, candidates, target)


def test_two_sum_case_1():
    # arrange
    candidates: list[int] = [2, 3, 6, 7]
    target: int = 7
    expected: list[list[int]] = [[2, 2, 3], [7]]

    # act
    solution = Solution()
    actual = solution.combinationSum(candidates, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_two_sum_case_2():
    # arrange
    candidates: list[int] = [2, 3, 5]
    target: int = 8
    expected: list[list[int]] = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # act
    solution = Solution()
    actual = solution.combinationSum(candidates, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_two_sum_case_3():
    # arrange
    candidates: list[int] = [2]
    target: int = 1
    expected: list[list[int]] = []

    # act
    solution = Solution()
    actual = solution.combinationSum(candidates, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
