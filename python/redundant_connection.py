class DSU:
    def __init__(self, n: int):
        self._parents: list[int] = [i for i in range(n + 1)]
        self._rank: list[int] = [1] * (n + 1)

    def find(self, node: int) -> int:
        curr: int = node
        while curr != self._parents[curr]:
            self._parents[curr] = self._parents[self._parents[curr]]
            curr = self._parents[curr]
        return curr

    def union(self, u: int, v: int) -> bool:
        ru: int = self.find(u)
        rv: int = self.find(v)
        if ru == rv:
            return False
        if self._rank[ru] < self._rank[rv]:
            ru, rv = rv, ru
        self._rank[ru] += self._rank[rv]
        self._parents[rv] = ru
        return True


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """time complexity: O(E + a(V)), where E is the number of edges and V is the number of vertices"""
        dsu: DSU = DSU(len(edges))
        for u, v in edges:
            if dsu.union(u, v):
                continue
            return [u, v]
        return []


def test_findRedundantConnection_case_1():
    # arrange
    edges: list[list[int]] = [[1, 2], [1, 3], [2, 3]]
    expected: list[int] = [2, 3]

    # act
    solution = Solution()
    actual = solution.findRedundantConnection(edges)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_findRedundantConnection_case_2():
    # arrange
    edges: list[list[int]] = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

    expected: list[int] = [1, 4]

    # act
    solution = Solution()
    actual = solution.findRedundantConnection(edges)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
