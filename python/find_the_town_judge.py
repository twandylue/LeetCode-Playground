from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        """timc complexity: O(n), where n is the number of people. space complexity: O(n)"""
        outgoing: dict[int, list[int]] = defaultdict(list)
        incoming: dict[int, list[int]] = defaultdict(list)
        for src, dst in trust:
            outgoing[src].append(dst)
            incoming[dst].append(src)
        for i in range(1, n + 1):
            if len(outgoing[i]) == 0 and len(incoming[i]) == n - 1:
                return i
        return -1


def test_findJudge_case_1():
    # arrange
    n: int = 2
    trust: list[list[int]] = [[1, 2]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.findJudge(n, trust)

    # assert
    assert expected == actual


def test_findJudge_case_2():
    # arrange
    n: int = 3
    trust: list[list[int]] = [[1, 3], [2, 3]]
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.findJudge(n, trust)

    # assert
    assert expected == actual


def test_findJudge_case_3():
    # arrange
    n: int = 3
    trust: list[list[int]] = [[1, 3], [2, 3], [3, 1]]
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.findJudge(n, trust)

    # assert
    assert expected == actual


def test_findJudge_case_4():
    # arrange
    n: int = 3
    trust: list[list[int]] = [[1, 2], [2, 3]]
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.findJudge(n, trust)

    # assert
    assert expected == actual
