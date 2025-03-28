class UnionFind:
    def __init__(self, n: int):
        self._ranks: list[int] = [1] * (n + 1)
        self._parents: list[int] = [i for i in range(n + 1)]

    def find(self, n: int) -> int:
        while n != self._parents[n]:
            n = self._parents[n]
        return n

    def union(self, u: int, v: int) -> bool:
        pu: int = self.find(u)
        pv: int = self.find(v)
        if pu == pv:
            return False
        if self._ranks[pv] > self._ranks[pu]:
            pu, pv = pv, pu
        self._ranks[pu] += self._ranks[pv]
        self._parents[pv] = pu
        return True


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """time complexity: O(E + a(V)), where E is the number of edges and V is the number of vertices"""
        uf: UnionFind = UnionFind(len(edges))
        for u, v in edges:
            if not uf.union(u, v):
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
