from collections import defaultdict
from math import sqrt


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        """time complexity: O(n^2), space complexity: O(n)"""
        graph: dict[int, list[int]] = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d: int = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if d <= r1:
                    graph[i].append(j)
                if d <= r2:
                    graph[j].append(i)
        result: int = 0
        for i in range(len(bombs)):
            result = max(result, self.dfs(i, set(), graph))
        return result

    def dfs(self, node: int, visited: set[int], graph: dict[int, list[int]]) -> int:
        if node in visited:
            return 0
        visited.add(node)
        result: int = 1
        for nei in graph[node]:
            result += self.dfs(nei, visited, graph)
        return result


def test_maximumDetonation_case_1():
    # arrange
    bombs: list[list[int]] = [[2, 1, 3], [6, 1, 4]]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.maximumDetonation(bombs)

    # assert
    assert expected == actual


def test_maximumDetonation_case_2():
    # arrange
    bombs: list[list[int]] = [[1, 1, 5], [10, 10, 5]]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.maximumDetonation(bombs)

    # assert
    assert expected == actual


def test_maximumDetonation_case_3():
    # arrange
    bombs: list[list[int]] = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.maximumDetonation(bombs)

    # assert
    assert expected == actual
