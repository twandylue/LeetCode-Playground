from collections import defaultdict


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        """time complexity: O(n), where n is the number of edges. space complexity: O(n)"""
        incoming: dict[int, list[int]] = defaultdict(list)
        result: list[int] = []
        for src, dst in edges:
            incoming[dst].append(src)
        for i in range(n):
            if len(incoming[i]) == 0:
                result.append(i)
        return result


def test_findSmallestSetOfVertices_case_1():
    # arrange
    n: int = 6
    edges: list[list[int]] = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    expected: list[int] = [0, 3]

    # act
    solution = Solution()
    actual = solution.findSmallestSetOfVertices(n, edges)

    # assert
    assert expected == actual


def test_findSmallestSetOfVertices_case_2():
    # arrange
    n: list[int] = 5
    edges: list[list[int]] = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    expected: list[int] = [0, 2, 3]

    # act
    solution = Solution()
    actual = solution.findSmallestSetOfVertices(n, edges)

    # assert
    assert expected == actual
