class UnionFind:
    def __init__(self, n: int):
        self._parents: list[int] = [i for i in range(n)]
        self._ranks: list[int] = [1] * n

    def find(self, n: int) -> int:
        curr: int = n
        while curr != self._parents[curr]:
            self._parents[curr] = self._parents[self._parents[curr]]
            curr = self._parents[curr]
        return curr

    def union(self, u: int, v: int) -> bool:
        ru: int = self.find(u)
        rv: int = self.find(v)
        if ru == rv:
            return False
        if self._ranks[ru] > self._ranks[rv]:
            self._ranks[ru] += self._ranks[rv]
            self._parents[rv] = ru
        else:
            self._ranks[rv] += self._ranks[ru]
            self._parents[ru] = rv
        return True


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """time complexity: O(E + a(V)), where E is the number of edges and V is the number of vertices"""
        result: int = n
        uf: UnionFind = UnionFind(n)
        for u, v in edges:
            if uf.union(u, v):
                result -= 1
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
