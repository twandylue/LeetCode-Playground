class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []
        self.dfs(0, 0, candidates, target, [], result)

        return result

    def dfs(
        self,
        i: int,
        accu: int,
        candidates: list[int],
        target: int,
        subset: list[int],
        result: list[list[int]],
    ) -> None:
        if accu == target:
            result.append(subset[:])
            return
        elif accu > target or i >= len(candidates):
            return

        subset.append(candidates[i])
        self.dfs(i, accu + candidates[i], candidates, target, subset, result)
        subset.pop()
        self.dfs(i + 1, accu, candidates, target, subset, result)


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
