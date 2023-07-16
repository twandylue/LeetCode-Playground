class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result: list[list[int]] = []
        self.dfs(0, candidates, [], result, target)

        return result

    def dfs(
        self,
        pos: int,
        candidates: list[int],
        subset: list[int],
        result: list[list[int]],
        target: int,
    ):
        if target == 0:
            result.append(subset[:])
            return
        elif target < 0:
            return

        prev: int = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            subset.append(candidates[i])
            self.dfs(i + 1, candidates, subset, result, target - candidates[i])
            subset.pop()
            prev = candidates[i]

        return result


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
