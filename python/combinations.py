class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """time complexity: O(n!)"""
        result: list[list[int]] = []
        subset: list[int] = []
        self.dfs(1, n, k, subset, result)
        return result

    def dfs(
        self, num: int, n: int, k: int, subset: list[int], result: list[list[int]]
    ) -> None:
        if num > n + 1:
            return
        if len(subset) == k:
            result.append(subset.copy())
        for i in range(num, n + 1):
            subset.append(i)
            self.dfs(i + 1, n, k, subset, result)
            subset.pop()


def test_combine_case_1():
    # arrange
    n: int = 4
    k: int = 2
    expected: list[list[int]] = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    # act
    actual = Solution().combine(n, k)

    # assert
    assert expected == actual


def test_combine_case_2():
    # arrange
    n: int = 1
    k: int = 1
    expected: list[list[int]] = [[1]]

    # act
    actual = Solution().combine(n, k)

    # assert
    assert expected == actual
