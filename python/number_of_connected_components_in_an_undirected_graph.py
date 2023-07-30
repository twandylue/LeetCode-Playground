class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        result: int = n
        parents: list[int] = [i for i in range(0, n)]
        rank: list[int] = [1] * n
        for edge in edges:
            result -= self.union(edge[0], edge[1], rank, parents)

        return result

    def find(self, n: int, parents: list[int]) -> int:
        node: int = n
        while node != parents[node]:
            # TODO:
            parents[node] = parents[parents[node]]
            node = parents[node]

        return node

    def union(self, n1: int, n2: int, rank: list[int], parents: list[int]) -> int:
        if n1 == n2:
            return 0
        if rank[n1] > rank[n2]:
            rank[n1] += rank[n2]
            parents[n2] = n1
        else:
            rank[n2] += rank[n1]
            parents[n1] = n2
        return 1


def test_countComponents_case_1():
    # arrange
    n: int = 5
    edges: list[list[int]] = [[0, 1], [1, 2], [3, 4]]
    expected = 2

    # act
    solution = Solution()
    actual = solution.countComponents(n, edges)

    # assert
    assert expected == actual


def test_countComponents_case_2():
    # arrange
    n: int = 5
    edges: list[list[int]] = [[0, 1], [1, 2], [3, 4]]
    expected = 2

    # act
    solution = Solution()
    actual = solution.countComponents(n, edges)

    # assert
    assert expected == actual
