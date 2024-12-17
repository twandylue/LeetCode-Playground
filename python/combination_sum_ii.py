class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """time complexity: O(n * 2^n)"""
        result: list[list[int]] = []
        accu_set: list[int] = []
        accu: int = 0
        candidates.sort()
        self.dfs(0, accu, accu_set, result, candidates, target)
        return result

    def dfs(
        self,
        i: int,
        accu: int,
        accu_set: list[int],
        result: list[list[int]],
        candidates: list[int],
        target: int,
    ) -> None:
        if accu == target:
            result.append(accu_set.copy())
            return
        if i >= len(candidates) or accu > target:
            return
        accu_set.append(candidates[i])
        self.dfs(i + 1, accu + candidates[i], accu_set, result, candidates, target)
        accu_set.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        self.dfs(i + 1, accu, accu_set, result, candidates, target)


def test_combinationSum2_case_1():
    # arrange
    candidates: list[int] = [10, 1, 2, 7, 6, 1, 5]
    target: int = 8
    expected: list[list[int]] = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    # act
    solution = Solution()
    actual = solution.combinationSum2(candidates, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_combinationSum2_case_2():
    # arrange
    candidates: list[int] = [2, 5, 2, 1, 2]
    target: int = 5
    expected: list[list[int]] = [[1, 2, 2], [5]]

    # act
    solution = Solution()
    actual = solution.combinationSum2(candidates, target)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
