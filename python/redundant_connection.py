class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent: list[int] = [i for i in range(0, len(edges) + 1)]
        rank: list[int] = [1] * (len(edges) + 1)

        for n1, n2 in edges:
            if self.union(n1, n2, rank, parent):
                continue
            return [n1, n2]

        return []

    def find(self, n: int, parent: list[int]) -> int:
        p: int = parent[n]
        while p != parent[p]:
            p = parent[p]
            parent[p] = parent[parent[p]]

        return p

    def union(self, n1: int, n2: int, rank: list[int], parent: list[int]) -> bool:
        p1: int = self.find(n1, parent)
        p2: int = self.find(n2, parent)

        if p1 == p2:
            return False
        if rank[p1] < rank[p2]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]

        return True


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
