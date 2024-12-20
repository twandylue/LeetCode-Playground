class UnionFind:
    def __init__(self, n: int):
        self._parents: list[int] = [i for i in range(n)]
        self._ranks: list[int] = [1] * n

    def find(self, n: int) -> int:
        while n != self._parents[n]:
            tmp: int = self._parents[n]
            self._parents[n] = self._parents[self._parents[n]]
            n = tmp
        return n

    def union(self, x1: int, x2: int) -> int:
        p1: int = self.find(x1)
        p2: int = self.find(x2)
        if p1 == p2:
            return 0
        if self._ranks[p1] > self._ranks[p2]:
            self._ranks[p1] += self._ranks[p2]
            self._parents[p2] = p1
        else:
            self._ranks[p2] += self._ranks[p1]
            self._parents[p1] = p2
        return 1


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """time complexity: O(E + V), where E is the number of edges and V is the number of vertices"""
        result: int = n
        uf: UnionFind = UnionFind(n)
        for edge in edges:
            result -= uf.union(edge[0], edge[1])
        return result

    def countComponents2(self, n: int, edges: list[list[int]]) -> int:
        visited: list[bool] = [False] * n
        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result: int = 0
        for node in range(n):
            if visited[node]:
                continue
            visited[node] = True
            result += 1
            self.dfs(node, visited, adj)
        return result

    def dfs(self, node: int, visited: list[bool], adj: list[list[int]]) -> None:
        for nei in adj[node]:
            if visited[nei]:
                continue
            visited[nei] = True
            self.dfs(nei, visited, adj)


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
    n: int = 6
    edges: list[list[int]] = [[0, 1], [2, 3], [4, 5]]
    expected = 3

    # act
    solution = Solution()
    actual = solution.countComponents(n, edges)

    # assert
    assert expected == actual
